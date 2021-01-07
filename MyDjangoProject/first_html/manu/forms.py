from django import forms
class manuCreateForm(forms.Form):
    name=forms.CharField(max_length=120)
    age=forms.IntegerField()
    course=forms.CharField(max_length=150)

