from django.shortcuts import render,redirect
from employee.forms import employeeForm
from employee.models import Employee


# Create your views here.

def employeeDetails(request):
    form=employeeForm()
    context={}
    context["form"]=form
    if request.method=='POST':
        form=employeeForm(request.POST)
        if form.is_valid():
            age=form.cleaned_data.get("age")
            salary=form.cleaned_data.get("salary")
            employee=Employee(age=age,salary=salary)
            employee.save()
            return redirect("employeelist")

    return render(request,"employee/employeecreate.html",context)

def employeeModel(request):
    employee=Employee.objects.all()
    context={}
    context["employee"]=employee
    return render(request,"employee/employeelist.html",context)


