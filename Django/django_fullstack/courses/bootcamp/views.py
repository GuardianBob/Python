from django.shortcuts import render, redirect
from .models import Course, Descr
from django.contrib import messages

def index(request):
    context = {
        'courses': Descr.objects.all()
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == 'GET':
        return redirect('/')
    errors = Descr.objects.basic_validator(request.POST)
    ttl = Course.objects.filter(title=request.POST['title'])
    if len(ttl) != 0:
        errors["title"] = "Course already exists!"
        # check if the errors dictionary has anything in it    
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        context = {
            'courses': Descr.objects.all(),
            'title': request.POST['title'],            
            'descr': request.POST['descr'],
            'errors': errors
        }
        return render(request, 'index.html', context)    
    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the show to be created, make the changes, and save        
        title = request.POST['title']
        course = Course.objects.create(title=title)
        Descr.objects.create(course=course, descr=request.POST['descr'])
        return redirect('/')

def destroy(request, uid):
    delete_show = Course.objects.get(id=uid)
    delete_show.delete()
    return redirect('/')