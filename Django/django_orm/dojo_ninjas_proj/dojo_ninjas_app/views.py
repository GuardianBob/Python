from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def index(request):
    context = {
        'dojos':Dojo.objects.all(),
        'ninjas':Ninja.objects.all()
    }
    return render(request, 'index.html', context)

def submit(request):
    if request.method == 'GET':
        return redirect('/')
    if 'submitDojo' in request.POST:
        dName = request.POST['dName']
        dCity = request.POST['dCity']
        dState = request.POST['dState']
        descr = ''
        Dojo.objects.create(name=dName, city=dCity, state=dState, desc=descr)
    elif 'submitNinja' in request.POST:
        dojos = Dojo.objects.all()
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dName = request.POST['dojo']
        uid = ''
        for dojo in dojos:
            if dojo.name == dName:
                uid = dojo.id
        nDojo = Dojo.objects.get(id=uid)
        Ninja.objects.create(first_name=first_name, last_name=last_name, dojo=nDojo)
    return redirect('/')

def delete_ninja(request, fName, lName):
    ninjas = Ninja.objects.all()
    uid = ''
    for ninja in ninjas:
        if ninja.first_name == fName and ninja.last_name == lName:
            uid = ninja.id
    del1=Ninja.objects.get(id=uid)
    del1.delete()
    return redirect('/')

def delete_dojo(request, dName):
    dojos = Dojo.objects.all()
    uid = ''
    for dojo in dojos:
        if dojo.name == dName:
            uid = dojo.id
    del1=Dojo.objects.get(id=uid)
    del1.delete()
    return redirect('/')