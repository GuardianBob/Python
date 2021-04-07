from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.contrib.auth import logout
import bcrypt

def index(request):
    context = {'data': request.session}
    if 'errors' in request.session:    
        context.update({'errors': request.session['errors']})
    if 'lErrors' in request.session:
        context.update({'lErrors': request.session['lErrors']})
    return render(request, 'index.html', context)

def register(request):
    if request.method == "GET":
        return redirect("/")
    request.session.flush()
    errors = User.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        request.session['fName'] = request.POST['fName']
        request.session['lName'] = request.POST['lName']
        request.session['email'] = request.POST['email']
        request.session['birthday'] = request.POST['birthday']
        request.session['errors'] = errors    
        return redirect('/')  
    else:
        passwd = request.POST['passwd']
        uPass = bcrypt.hashpw(passwd.encode(), bcrypt.gensalt()).decode()
        User.objects.create(first_name=request.POST['fName'], last_name=request.POST['lName'], email=request.POST['email'], password=uPass, birthday=request.POST['birthday'])
        request.session['name'] = request.POST['fName']
        request.session["login"] = "registered"
        return redirect('/success')
    
def login(request):
    if request.method == "GET":
        return redirect("/")
    request.session.flush()
    passwd = bcrypt.hashpw(request.POST['passwd2'].encode(), bcrypt.gensalt())
    lErrors = User.objects.checkLogin(request.POST)
    if len(lErrors) > 0:
        for key, value in lErrors.items():
            messages.error(request, value)
            request.session['lErrors'] = lErrors
            request.session['email2'] = request.POST['email2']
        return redirect('/')
    else:
        usr = User.objects.get(email=request.POST['email2'])
        request.session["user_id"] = usr.id
        return redirect('/wall')

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

