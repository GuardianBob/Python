from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, "index.html")


def submit(request):
    if request.method == "POST":
        stacks = request.POST.getlist("stacks")
        count = request.POST.getlist("stacks")  
        count.pop()  
        request.session['info'] = {
            "valName": request.POST["usrName"],
            "valLoc": request.POST["usrLoc"],
            "valLang": request.POST["usrLang"],
            "valCmt": request.POST["comments"],
            "valClass": request.POST["class"],
            "valStacks": stacks,  
            "count": count
        }
        
        return redirect("/result")
    return redirect("/")
    
def result(request):    
    context = {
        'info': request.session['info']
    }   
    print(context)
    return render(request, "result.html", context)  
