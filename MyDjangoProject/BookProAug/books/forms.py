from django import forms
class BookCreateForm(forms.Form):
    book_name=forms.CharField(max_length=150)
    price=forms.IntegerField()
    pages=forms.IntegerField()
    author=forms.CharField(max_length=150)
