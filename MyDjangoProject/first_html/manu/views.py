from django.shortcuts import render,redirect
from manu.models import Manu
from manu.forms import manuCreateForm



# Create your views here.
def manudetails(request):
    form=manuCreateForm()
    context={}
    context["form"]=form
    return render(request,"manu/manudetails.html",context)

def manuGetDetails(request):
    name=request.POST.get("name")
    age= request.POST.get("age")
    course= request.POST.get("course")
    print(name,",",age,",",course)
    manu=Manu(name=name,age=age,course=course)
    manu.save()
    # return render(request,"manu/manudetails.html")
    return redirect("manumodeldetails")

def manuModelDetails(request):
    manu_det=Manu.objects.all()
    context={}
    context["manu_det"]=manu_det
    return render(request,"manu/listmanu.html",context)



