from django.shortcuts import render,redirect
from book.forms import bookCreateForm
from book.models import bookCreateModel
# Create your views here.

def createBook(request):
    form=bookCreateForm()
    context={}
    context["form"]=form
    if(request.method=='POST'):
        form=bookCreateForm(request.POST)
        if(form.is_valid()):
            bookname=form.cleaned_data.get("bookname")
            price=form.cleaned_data.get("price")
            pages=form.cleaned_data.get("pages")
            author=form.cleaned_data.get("author")
            book=bookCreateModel(bookname=bookname,price=price,pages=pages,author=author)
            book.save()
            return redirect("listbook")
    return render(request,"book/createbook.html",context)

def createModel(request):
    book=bookCreateModel.objects.all()
    context={}
    context["book"]=book
    return render(request,"book/listbook.html",context)


