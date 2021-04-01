from django.shortcuts import render, redirect
from .models import Show, Network

def check_network(netwk):
    nt = Network.objects.filter(name=netwk)
    if len(nt) == 0:
        Network.objects.create(name=netwk)
    all_nt = Network.objects.all()
    for network in all_nt:
        if network.name == netwk:
            return network

def index(request):
    return redirect('/shows')

def shows(request):
    context = {
        'shows':Show.objects.all()
    }
    return render(request, 'shows.html', context)

def new(request):
    
    return render(request, 'new.html')

def create(request):
    if request.method == 'GET':
        return redirect('/')
    show_title = request.POST['title']
    show_network = request.POST['network']
    show_release = request.POST['release']
    show_description = request.POST['description']
    s_network = check_network(show_network)
    print(s_network)
    Show.objects.create(title=show_title, description=show_description, release_date=show_release, network=s_network)
    return redirect('/shows')

def info(request, uid):
    context = {
        'show': Show.objects.get(id=uid)
    }
    return render(request, 'show.html', context)

def edit(request, uid):
    context = {
        'show': Show.objects.get(id=uid)
    }
    return render(request, 'edit.html', context)

def update(request, uid):
    update_show = Show.objects.get(id=uid)
    update_show.title = request.POST['title']    
    update_show.release_date = request.POST['release']
    update_show.description = request.POST['description']
    show_network = request.POST['network']
    update_show.network = check_network(show_network)
    update_show.save()
    return redirect('/shows')

def destroy(request, uid):
    delete_show = Show.objects.get(id=uid)
    delete_show.delete()
    return redirect('/shows')