from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, "index.html")


def submit(request):
    if request.method == "POST":
        stacks = request.POST.getlist("stacks")
        count = request.POST.getlist("stacks")
        request.session["valName"] = request.POST["usrName"]
        request.session["valLoc"] = request.POST["usrLoc"]
        request.session["valLang"] = request.POST["usrLang"]
        request.session["valCmt"] = request.POST["comments"]
        request.session["valClass"] = request.POST["class"]
        request.session["valStacks"] = stacks
        count.pop()
        request.session["count"] = count

        return redirect("/result")
    return redirect("/")
    
def result(request):
    return render(request, "result.html")  