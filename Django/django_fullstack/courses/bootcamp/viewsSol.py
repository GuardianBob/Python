from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    context = {
        "courses": Course.objects.all()
        }
    return render(request, 'index.html', context)

def create(request):
    errors = Course.objects.validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
    else:
        course = Course.objects.create(
            name=request.POST['course_name']
        )
        desc = Description.objects.create(content=request.POST['desc'])
        course.description = desc
        course.save()

    return redirect("/courses")

def delete(request,id):
  if request.method == "GET":
    context = {
        "course": Course.objects.get(id=id)
    }
    return render(request,'delete.html', context)

  if request.method == "POST":
    course = Course.objects.get(id=id)
    course.delete()
    return redirect("/courses")

def comments(request,id):
    context = {
        "course": Course.objects.get(id=id)
    }
    return render(request,'comments.html', context)

def create_comment(request, id):
    errors = Comment.objects.validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
    else:
        Comment.objects.create(
            content=request.POST['content'],
            course = Course.objects.get(id=id)
        )
    return redirect(f"/courses/{id}")

# ======================== Second Solution ==================================

from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "all_courses": Course.objects.all()
    }
    return render(request, "index.html", context)

def create_course(request):
    if request.method == "POST":
        errors = Course.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            course = Course.objects.create(name=request.POST['course_name'], description=request.POST['description'])
    return redirect('/')

def destroy_course(request, course_id):
    context = {
        'one_course': Course.objects.get(id=course_id)
    }
    return render(request, "delete_page.html", context)

def delete_course(request, course_id):
    if request.method == "POST":
        course_to_delete = Course.objects.get(id=course_id)
        course_to_delete.delete()
    return redirect('/')