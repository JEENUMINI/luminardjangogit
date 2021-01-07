from django.shortcuts import render

# Create your views here.

def trainerLogin(request):
    return render(request,"trainer/login.html")

def trainerRegistration(request):
    return render(request,"trainer/register.html")

def trainerLogGetDetails(request):
    email=request.POST.get("email")
    password=request.POST.get("password")
    print(email,",",password)
    return render(request,"trainer/register.html")

def trainerRegGetDetails(request):
    reg_email=request.POST.get("reg_email")
    reg_pwd=request.POST.get("reg_pwd")
    print(reg_email,",",reg_pwd)
    context={}
    context["email"]=reg_email
    context["pwd"]=reg_pwd
    return render(request,"trainer/trainercontext.html",context)