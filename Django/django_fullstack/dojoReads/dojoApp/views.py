from django.shortcuts import render, redirect
from loginApp.models import User
from .models import Book, Author, Review
from django.http import JsonResponse, HttpResponseRedirect
from django.core import serializers
from .forms import BookForm, ReviewForm
from django.contrib import messages
import pytz
from django.utils import timezone
import datetime


def books(request):
    if not 'user_id' in request.session:
        return redirect('/')
    # if 'infoError' in request.session:
    #     del request.session['infoError']
    user_id = request.session['user_id']
    # if 'postError' in request.session:
    #     new_form = BookForm(request.session['postError'])
    reviews = Review.objects.order_by('-created_at')[:3]
    context = {
        'reviews': reviews,
        "user": User.objects.get(id=user_id),
        'books': Book.objects.all()
    }
    return render(request, 'books.html', context)

def add(request):
    if not 'user_id' in request.session:
        return redirect('/')    
    user_id = request.session['user_id']
    # if 'postError' in request.session:
    #     new_form = BookForm(request.session['postError'])
    # new_form = BookForm()
    context = {
        # "new_form": new_form,
        "books": Book.objects.all(),
        "authors": Author.objects.all(),
        "user": User.objects.get(id=user_id),
        "rateScale": range(1, 6),        
    }
    if 'errors' in request.session:
        context['errors'] = request.session['errors']
    return render(request, "add.html", context)

def book_info(request, bid):
    user_id = request.session['user_id']
    book = Book.objects.get(id=bid)
    author = Author.objects.get(books__id=bid)
    reviews = Review.objects.filter(book=book)
    context = {
        # "new_form": new_form,
        "book": book,
        "reviews": reviews,
        "author": author,
        "user": User.objects.get(id=user_id),
        "rateScale": range(1, 6),
    }
    if 'errors' in request.session:
        context['errors'] = request.session['errors']    
    return render(request, "info.html", context)

def user_info(request, uid):
    user = User.objects.get(id=uid)
    reviews = Review.objects.filter(user=user)
    context = {
        'user': user,
        'reviews': reviews,
    }
    return render(request, "user.html", context)

def update(request, bid):
    if not request.method == "POST":
        return redirect('/')
    rErrors = Review.objects.validate_review(request.POST)
    if len(rErrors) > 0:   
        for key, value in rErrors.items():
            messages.error(request, value)
            request.session['errors'] = rErrors 
        return redirect(f'/books/{bid}')
    else:
        user = User.objects.get(id=request.session['user_id'])
        book = Book.objects.get(id=bid)
        review = Review.objects.create(review=request.POST['review'], rating=request.POST['rating'], book=book, user=user)
        return redirect(f'/cl/info/{bid}')

def clear(request, page, bid=None):
    if 'errors' in request.session:
        del request.session['errors']
    if page == 'info':
        return redirect(f'/books/{bid}')
    if page == 'new' or page == 'books':
        return redirect('/books')
    if page == 'add':
        return redirect('/books/add')
    if page == 'users':
        return redirect(f'/users/{bid}')

def newBook(request):
    if not request.method == "POST":
        return redirect('/')
    errors = Book.objects.validator(request.POST)    
    if len(errors) > 0:
        print(errors)
        for key, value in errors.items():
            messages.error(request, value)
        request.session['author'] = request.POST['author']
        request.session['title'] = request.POST['title']
        request.session['errors'] = errors    
        return redirect('/books/add')
    # if 'errors' in request.session:
    #     del request.session['errors']    
    if not 'authorSel' in request.POST or request.POST['authorSel'] == '':        
        author_obj = checkAuthor(request.POST['author'])
    else:
        # print("author = " + request.POST['authorSel'])
        author_obj = Author.objects.get(id=request.POST['authorSel'])
    user = User.objects.get(id=request.session['user_id'])
    new_book = Book.objects.create(title=request.POST['title'], uploaded_by=user)
    author_obj.books.add(new_book)
    if request.POST['review'] != '':
        new_review = Review.objects.create(review=request.POST['review'], rating=request.POST['rating'], book=new_book, user=user)        
    return redirect('/cl/new/0')

def del_review(request, rid):
    review = Review.objects.get(id=rid)
    bid = review.book.id
    if request.session['user_id'] == review.user.id:
        review.delete()
    return redirect(f'/books/{bid}')
    
def checkAuthor(authName):
    fName = authName.split(" ", 1)[0]
    lName = authName.split(" ", 1)[1]
    author_obj = Author.objects.filter(first_name__contains=fName).filter(last_name__contains=lName)
    print(len(author_obj))
    if len(author_obj) > 0:
        return author_obj
    else:
        new_author = Author.objects.create(first_name=fName, last_name=lName)
        return new_author


