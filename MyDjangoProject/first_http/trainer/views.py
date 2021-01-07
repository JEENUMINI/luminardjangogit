from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def trainerLogin(request):
    return HttpResponse("<h1>trainer login</h1>")

def trainerRegistration(request):
    return HttpResponse("<h1>trainer registration</h1>")