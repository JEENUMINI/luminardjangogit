from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from employee.models import Employee
from django.urls import reverse_lazy

# Create your views here.

class EmployeeCreate(CreateView):
    model = Employee
    fields = "__all__"
    template_name ="employee/employee_form.html"
    success_url = reverse_lazy("list")

class EmployeeList(ListView):
    model = Employee
    fields = "__all__"
    template_name = "employee/employee_list.html"
    context_object_name = "employees"

class EmployeeEdit(UpdateView):
    model = Employee
    fields = "__all__"
    template_name = "employee/employee_edit.html"
    success_url = reverse_lazy("list")
    context_object_name = "employees"

class EmployeeDetails(DetailView):
    model = Employee
    fields = "__all__"
    context_object_name = "employees"
    template_name = "employee/employee_detail.html"

class EmployeeDelete(DeleteView):
    model = Employee
    fields = "__all__"
    context_object_name = "employees"
    template_name = "employee/employee_delete.html"
    success_url = reverse_lazy("list")







