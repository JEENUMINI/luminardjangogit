from django.shortcuts import render

# Create your views here.
def trainerLogin(request):
    return render(request,"trainer/login.html")

def trainerRegistration(request):
    return render(request,"trainer/registration.html")

def getTrLogDetails(request):
    tr_emil=request.POST.get("tr_emil")
    tr_pwd= request.POST.get("tr_pwd")
    print("tr_emil=",tr_emil)
    print("tr_pwd=",tr_pwd)
    return render(request,"trainer/registration.html")

def getTrRegDetails(request):
    tr_first=request.POST.get("tr_first")
    tr_last=request.POST.get("tr_last")
    tr_address=request.POST.get("tr_address")
    print("tr_first=",tr_first)
    print("tr_last=", tr_last)
    print("tr_address=", tr_address)
    # return render(request,"trainer/login.html")
    context={}
    context["tr_first"]=tr_first
    return render(request,"trainer/trainercontext.html",context)