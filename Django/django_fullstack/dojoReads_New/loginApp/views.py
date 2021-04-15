from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.contrib.auth import logout
import bcrypt
from .forms import Register_Form, Login_Form

def index(request, register_form=Register_Form(), login_form=Login_Form()):
    context = {
        'login_form': login_form,
        'register_form' : register_form
        }
    return render(request, 'index.html', context)

def register(request):    
    if request.method != "POST":
        return redirect("/")
    check_form = Register_Form(request.POST)
    if not check_form.is_valid():
        login_form = Login_Form()
        context = { 
            'register_form': check_form,
            'login_form' : login_form 
            }        
        return render(request, 'index.html', context)
    else:
        passwd = request.POST['reg_password']
        uPass = bcrypt.hashpw(passwd.encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=uPass)
        request.session["user_id"] = user.id
        return redirect('/books')
    
def login(request):
    if request.method != "POST":
        return redirect("/")
    check_form = Login_Form(request.POST)
    if not check_form.is_valid():
        register_form = Register_Form()
        context = { 
            'register_form': register_form,
            'login_form' : check_form 
            }
        return render(request, 'index.html', context)
    else:
        user = User.objects.get(email=request.POST['login_email'])
        request.session["user_id"] = user.id
        return redirect('/books')

def success(request):
    if not 'name' in request.session: 
        return redirect('/')
    context = {
            'name': request.session['name'],
            'login': request.session["login"]
        }
    return render(request, 'success.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')

