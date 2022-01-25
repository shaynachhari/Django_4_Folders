from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


# def index(request):
#     return HttpResponse("Shayna")

def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    return redirect("/login")


def login(request):
    return HttpResponse('login page')
