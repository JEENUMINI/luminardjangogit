from django import forms

class createEmployeeForm(forms.Form):
    employeename=forms.CharField(max_length=150)
    age=forms.IntegerField()
    salary=forms.IntegerField()
    designation=forms.CharField(max_length=150)