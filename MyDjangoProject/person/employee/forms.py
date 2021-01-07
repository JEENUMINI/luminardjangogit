from django import forms

class employeeForm(forms.Form):
    age=forms.IntegerField()
    salary=forms.IntegerField()
