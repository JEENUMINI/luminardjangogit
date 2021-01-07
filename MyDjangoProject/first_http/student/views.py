from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def studentLogin(request):
    return HttpResponse("<h1>student login</h1>")

def studentRegistration(request):
    return HttpResponse("<h1>student registration</h1>")
