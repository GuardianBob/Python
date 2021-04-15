from django.shortcuts import render, redirect
from loginApp.models import User
from .models import Message, Comment
from django.http import JsonResponse, HttpResponseRedirect
from django.core import serializers
from .forms import MessageForm, CommentForm, UpdateUserForm, UpdatePasswordForm
from loginApp.forms import Register_Form
from django.contrib import messages
import bcrypt
from django.utils import timezone
import datetime

# Create your views here.
def get_nav(request):
    nav = 'nav_out.html'
    if 'user_id' in request.session:
        nav = "nav_in.html"
    return nav

def validate_user(user_id):
    user = User.objects.get(id=user_id)
    return user.user_level

def admin(request):
    
    context = {
        'page_title' : 'Admin Dashboard',        
    }

def dashboard(request):
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'nav': get_nav(request),
        'admin' : user.user_level,
        'users' : User.objects.all(),
        'user_id': user.id,
        'page_title': 'Dashboard',
    }
    return render(request, 'dashboard.html', context)

def new_user(request):
    user_id = request.session['user_id']
    if validate_user(user_id) is False:
        return redirect('/dashboard')
    form = Register_Form()
    context = {
        'nav': get_nav(request),
        'user_id': user_id,
        'register_form': form,
        'page_title': 'Add User',
    }
    return render(request, 'add_user.html', context)


def edit_profile(request):
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'nav': get_nav(request),
        'admin' : user.user_level,
        'user': user,
        'user_id': user.id,
        'page_title': 'Edit Profile',
        'form_title': 'profile',
    }
    return render(request, 'edit_user.html', context)


def show_user(request, user_id):
    pass

def edit_user(request, user_id):
    context = {
        'form' : UpdateUserForm(),
        'password_form' : UpdatePasswordForm(),
        'update': '',
    }    
    return render_edit_page(request, context, user_id)
    # current_user = User.objects.get(id=request.session['user_id'])
    # if validate_user(current_user.id) is True:
    #     user = User.objects.get(id=user_id)
    #     form_title = 'User ' + str(user_id)
    # else:
    #     user = User.objects.get(id=request.session['user_id'])
    #     form_title = 'Profile'
    # form = UpdateUserForm()
    # password_form = UpdatePasswordForm()
    # user_level = "Normal"
    # if user.user_level is True:
    #     user_level = "Admin"
    # context = {
    #     'nav': get_nav(request),
    #     'admin' : current_user.user_level,
    #     'user': user,
    #     'user_id': user.id,
    #     'form': form,
    #     'password_form': password_form,
    #     'form_title': form_title,
    #     'page_title': 'Edit' + form_title,
    #     'level_select': ['Normal','Admin'],
    #     'user_level': user_level,
    # }
    # return render(request, 'edit_user.html', context)


def render_edit_page(request, context, user_id):
    current_user = User.objects.get(id=request.session['user_id'])
    if validate_user(current_user.id) is True:
        user = User.objects.get(id=user_id)
        form_title = 'User ' + str(user_id)
    else:
        user = User.objects.get(id=request.session['user_id'])
        form_title = 'Profile'    
    user_level = "Normal"
    if current_user.user_level is True:
        user_level = "Admin"
    add_info = {
        'nav': get_nav(request),
        'admin' : current_user.user_level,
        'user': user,
        'user_id': user.id,
        'form_title': form_title,
        'page_title': 'Edit' + form_title,
        'level_select': ['Normal','Admin'],
        'user_level': user_level,
    }
    context.update(add_info)
    return render(request, 'edit_user.html', context)

def update_password(request):
    check_form = UpdatePasswordForm(request.POST)
    if not check_form.is_valid():
        password_form = Register_Form()
        context = { 
            'password_form' : check_form,
            'form': UpdateUserForm(),
            'user_id': request.POST['user_id'],
            }
        return render_edit_page(request, context, request.POST['user_id'])
    else:
        user = User.objects.get(id=request.POST['user_id'])
        password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        user.password = password
        user.save()
        print('success!')
        return success(request, request.POST['user_id'])

def success(request, user_id):
    context = {
        'form' : UpdateUserForm(),
        'password_form' : UpdatePasswordForm(),
        'update': 'Update successful!',
        }
    return render_edit_page(request, context, user_id)

def update_user(request):
    check_form = UpdateUserForm(request.POST)
    if not check_form.is_valid():
        current_user = User.objects.get(id=request.session['user_id'])
        if validate_user(current_user.id) is True:
            user = User.objects.get(id=request.session['user_id'])
            form_title = 'User ' + str(request.session['user_id'])
        else:
            user = User.objects.get(id=request.session['user_id'])
            form_title = 'Profile'    
        user_level = "Normal"
        if current_user.user_level is True:
            user_level = "Admin"
        context = { 
            'password_form' : UpdatePasswordForm(),
            'form': check_form,
            'user_id': request.POST['user_id'],
            'nav': get_nav(request),
            'admin' : current_user.user_level,
            'user': user,
            'user_id': user.id,
            'form_title': form_title,
            'page_title': 'Edit' + form_title,
            'level_select': ['Normal','Admin'],
            'user_level': user_level,            
            }
        print('failed!', check_form)
        # return render_edit_page(request, context, request.POST['user_id'])
        return render(request, 'edit_user.html', context)
    else:
        
        user = User.objects.get(id=request.POST['user_id'])
        user.email = request.POST['email']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.user_level = request.POST['user_level']
        user.save()
        print('success!')
        return success(request, request.POST['user_id'])

def remove_user(request, user_id):
    user_id = request.session['user_id']
    if validate_user(user_id) is False:
        return redirect('/dashboard')
    pass