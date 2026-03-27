from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello guys , you are at my first Django project's home page")
    return render(request, 'website\index.html')

def about(request):
    return HttpResponse("Hello guys , you are at my first Django project's about page")


def contact(request):
    return HttpResponse("Hello guys , you are at my first Django project's contact page")