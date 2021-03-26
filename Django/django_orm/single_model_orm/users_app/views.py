from django.shortcuts import render
from .models import User

def index(request):
    context = {
        "all_users": User.objects.all()
    }
    return render(request, 'index.html', context)
 
def new_user(requests):
    nUsr = User.Objects.create()
    nUsr.first_name = request.sessions.POST('fName')
    nUsr.last_name = request.sessions.POST('lName')
    nUsr.email_address = request.sessions.POST('email')
    nUsr.age = request.sessions.POST('age')
    nUsr.save()
    return redirect('/')
