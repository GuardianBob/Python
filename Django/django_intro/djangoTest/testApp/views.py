from django.shortcuts import render, HttpResponse, redirect
import json, requests

POKEURL = 'https://pokeapi.co/api/v2/pokemon/'
IMGURL = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/'


def index(request):
    if 'pokeid' not in request.session or 'pokeimg' not in request.session:
        request.session['pokeid'] = ''
        request.session['pokeimg'] = ''
    context = {
        'pokeid': request.session['pokeid'],
        'pokeimg': request.session['pokeimg']
    }
    return render(request, 'index.html', context)

def get(request):
    pId = request.POST['poke']
    request.session['pokeimg'] = IMGURL + pId + '.svg'
    pUrl = requests.get(POKEURL + pId + '/')
    y = pUrl.json()
    pName = y['name']
    pName = pName.capitalize()
    request.session['pokeid'] = pName
    print(request.session['pokeimg'], request.session['pokeid'])
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')
