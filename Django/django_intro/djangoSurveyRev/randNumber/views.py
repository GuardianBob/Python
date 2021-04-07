from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.

def index(request):
    
    if not "count" in request.session: 
        request.session["count1"] = 0
    rand = get_random_string(length=14)
    request.session["rand"] = rand.upper()
    num1 = request.session["count1"]
    num1 += 1
    request.session["count1"] = num1
    context = {
        "count": request.session["count1"],
        "newWord": request.session["rand"]
    }
    return render(request, "rand.html", context)

def get(request):
    return redirect('/random_word')

def reset(request):
    request.session["count1"] = 0
    return redirect('/random_word')
