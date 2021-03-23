from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, "index.html")

def result(request):
    if request.method == "POST":
        stacks = request.POST.getlist("stacks")
        context = {
            "valName": request.POST["usrName"],
            "valLoc": request.POST["usrLoc"],
            "valLang": request.POST["usrLang"],
            "valCmt": request.POST["comments"],
            "valClass": request.POST["class"],
            "valStacks": stacks
        }
        return render(request, "result.html", context)
        
