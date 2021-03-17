from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("Placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("Placeholder to display a new form to create a new blog")

def create(request):
    return  redirect("/")

def show(request, number):
    nStr = f'placeholder to display blog number: {number}'
    return HttpResponse(nStr)

def edit(request, number):
    nStr = f'placeholder to edit blog number: {number}'
    return HttpResponse(nStr)

def destroy(request, number):
    return  redirect("/")

# Create your views here.