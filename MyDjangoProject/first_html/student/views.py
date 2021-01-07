from django.shortcuts import render


# Create your views here.
def studentLogin(request):
    return render(request,"student/login.html")

def studentRegistration(request):
    return render(request,"student/registration.html")

def getRegDetails(request):
    firstname=request.POST.get("firstname")
    lastname = request.POST.get("lastname")
    address=request.POST.get("address")
    print("firstname=",firstname)
    print("lastname=",lastname)
    print("address=",address)

    return render(request,"student/login.html")

def getLogDetails(request):
    email=request.POST.get("email")
    password=request.POST.get("password")
    print("email=",email)
    print("password=",password)
    # return render(request, "student/registration.html")
    context={}
    context["name"]=email
    context["password"]=password
    return render(request,"student/studentcontext.html",context)
