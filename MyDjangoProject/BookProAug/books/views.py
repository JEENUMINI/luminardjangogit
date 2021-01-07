from django.shortcuts import render,redirect
from books.models import Book
from books.forms import BookCreateForm

# Create your views here.

def createBook(request):
    form=BookCreateForm()
    context={}
    context["form"]=form
    if request.method=='POST':
        form=BookCreateForm(request.POST)
        if form.is_valid():
            book_name=form.cleaned_data.get("book_name")
            price=form.cleaned_data.get("price")
            pages=form.cleaned_data.get("pages")
            author=form.cleaned_data.get("author")
            book=Book(book_name=book_name,price=price,pages=pages,author=author)
            book.save()
            return redirect("getbooks")
    return render(request,"books/bookcreate.html",context)



def getBooks(request):
    books=Book.objects.all()
    context={}
    context["books"]=books
    return render(request,"books/listbooks.html",context)