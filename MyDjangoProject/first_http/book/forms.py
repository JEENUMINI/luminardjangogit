from django import forms

class bookForms(forms.Form):
    name=forms.CharField(max_length=150)
    price=forms.IntegerField()
    pages=forms.IntegerField()
