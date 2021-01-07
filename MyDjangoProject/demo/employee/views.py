from django.shortcuts import render,redirect
from employee.forms import createEmployeeForm
from employee.models import createEmployeeModel

# Create your views here.
def createEmployee(request):
    form=createEmployeeForm()
    context={}
    context["form"]=form
    if(request.method=='POST'):
        form=createEmployeeForm(request.POST)
        if(form.is_valid()):
            employeename=form.cleaned_data.get("employeename")
            age=form.cleaned_data.get("age")
            salary=form.cleaned_data.get("salary")
            designation=form.cleaned_data.get("designation")
            employee=createEmployeeModel(employeename=employeename,age=age,salary=salary,designation=designation)
            employee.save()
            return redirect("employeelist")
    return render(request,"employee/createemployee.html",context)




def employeeModel(request):
    employee=createEmployeeModel.objects.all()
    context={}
    context["employee"]=employee
    return render(request,"employee/employeelist.html",context)


