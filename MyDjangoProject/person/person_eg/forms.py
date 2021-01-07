from django import forms
class PersonCreateForm(forms.Form):
    person_name=forms.CharField(max_length=120)
    age=forms.IntegerField()
    salary=forms.IntegerField()
    designation=forms.CharField(max_length=120)

