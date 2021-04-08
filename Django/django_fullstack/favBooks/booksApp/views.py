from django.shortcuts import render, redirect, HttpResponse
from .models import Book, Author
from loginApp.models import User
from django.http import JsonResponse
from django.core import serializers
from .forms import BookForm
from django.contrib import messages 

def main(request):    
    if not 'user_id' in request.session:
        return redirect('/')
    if 'infoError' in request.session:
        del request.session['infoError']
    user_id = request.session['user_id']
    if 'postError' in request.session:
        new_form = BookForm(request.session['postError'])
    else:
        new_form = BookForm()    
    context = {
        "new_form": new_form,
        "books": Book.objects.all(),
        "user": User.objects.get(id=user_id)
    }
    # if request.POST:
    #     if not new_form.is_valid():
    #         messages.error(request, "Error")
    return render(request, "main.html", context)

def new_book(request):
    if request.is_ajax and request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            user = User.objects.get(id=request.session['user_id'])
            instance = form.save(commit=False)
            instance.uploaded_by = user            
            instance.save()
            instance.liked_by.add(user)
            if 'postError' in request.session:
                del request.session['postError']
        else:
            request.session['postError'] = request.POST    
    return redirect('/main')
    

def update(request):
    print("submitted")
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            user = User.objects.get(id=request.session['user_id'])
            instance = Book.objects.get(id=request.session['book_id'])
            instance.title = request.POST['title']
            instance.desc = request.POST['desc']
            instance.save()
            if 'infoError' in request.session:
                del request.session['infoError']
        else:
            request.session['infoError'] = request.POST
    return redirect('/main')

def delete(request, uid):
    book = Book.objects.get(id=uid)
    user = User.objects.get(id=request.session['user_id'])
    if book.uploaded_by.id == user.id:
        book.delete()
    return redirect('/main')

def info(request, uid):
    book = Book.objects.get(id=uid)
    request.session['book_id'] = uid
    if 'postError' in request.session:
        del request.session['postError']
    if 'infoError' in request.session:
        form = BookForm(request.session['infoError'])
    else:
        form = BookForm(book)
    context = {
        'book': book,
        "user": User.objects.get(id=request.session['user_id']),
        "form": form
    }
    return render(request, "info.html", context)

def add_favorite(request, uid, page):
    book = Book.objects.get(id=uid)
    user = User.objects.get(id=request.session['user_id'])
    book.liked_by.add(user)
    book.save()
    return redirect('/main')

def remove_favorite(request, uid, page):
    book = Book.objects.get(id=uid)
    user = User.objects.get(id=request.session['user_id'])
    book.liked_by.remove(user)
    book.save()
    return redirect('/main')
    # return HttpResponse("removed") #redirect('/' + page)