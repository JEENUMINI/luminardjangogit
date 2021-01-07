from django import forms

class bookCreateForm(forms.Form):
    bookname=forms.CharField(max_length=150)
    price=forms.IntegerField()
    pages=forms.IntegerField()
    author=forms.CharField(max_length=150)

