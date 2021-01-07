from django.shortcuts import render

# Create your views here.
def studLogin(request):
    return render(request,"student/login.html")

def studRegistration(request):
    return render(request,"student/registration.html")

def studGetLogDetails(request):
    username=request.POST.get("username")
    lastname=request.POST.get("lastname")
    print(username,",",lastname)
    return render(request,"student/registration.html")

def studGetRegDetails(request):
    reg_fi=request.POST.get("reg_fi")
    reg_la=request.POST.get("reg_la")
    print(reg_fi,reg_la)
    context={}
    context["name"]=reg_fi
    context["second_name"]=reg_la
    return render(request,"student/studentcontext.html",context)
