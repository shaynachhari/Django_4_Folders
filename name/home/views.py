from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
    # save krlo yrr fike


def login(request):
    return render(request, 'login.html')

# Create your views here.
