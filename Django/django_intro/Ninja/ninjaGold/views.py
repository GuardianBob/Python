from django.shortcuts import render, redirect
from random import randint
import datetime

# Create your views here.
def index(request):
    if 'gold1' not in request.session:
        request.session['gold1'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    context = {
        'goldCount': request.session['gold1'],
        'activities': request.session['activities']
    }
    return render(request, 'index.html', context)

def process_money(request, loc, highV, lowV):        
    if loc == 'Casino':
        lowV = 0 - highV
    gold = randint(lowV, highV)    
    dt = datetime.datetime.now()
    dtStr = dt.strftime('%Y/%m/%d %H:%M %p')
    if gold >= 0:
        upDn = 'Earned'
    else:
        upDn = 'Lost'
    updt = f'{ upDn } { gold } golds from the { loc }! ({ dtStr })'    
    request.session['gold1'] += gold
    request.session['activities'].append(updt)
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')