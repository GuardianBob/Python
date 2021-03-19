from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.
def index(request):
    x = datetime.datetime.now()
    context = {
        "date": x.strftime("%B %d, %Y"),
        "time": x.strftime("%H:%M %p")
    }
    return render(request, "index.html", context)