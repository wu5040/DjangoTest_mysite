from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello Django!")

def article(request,id):
    if id==1:
        return HttpResponse("article 1")
    else:
        return HttpResponse("article else")