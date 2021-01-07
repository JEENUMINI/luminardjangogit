from django.shortcuts import render

# Create your views here.
def taskPerform(request):
    return render(request,"task/task.html")
def taskGetDetails(request):
    num1=request.POST.get("num1")
    num2= request.POST.get("num2")
    res=int(num1)+int(num2)
    print("first_value=",num1)
    print("second_value=",num2)
    print(res)
    context={}
    context["num1"]=num1
    context["num2"]=num2
    context["res"]=res
    return render(request,"task/taskcontext.html",context)
