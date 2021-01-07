from django.shortcuts import render,redirect
from book.models import bookModel
from book.forms import bookForms

# Create your views here.
def createbook(request):
    # return render(request,"book/createbook.html")
    form=bookForms()
    context={}
    context["form"]=form
    return render(request,"book/createbook.html",context)

def getDetailsTerminal(request):
    name=request.POST.get("name")
    price=request.POST.get("price")
    pages=request.POST.get("pages")
    print(name,",",price,",",pages)
    book=bookModel(name=name,price=price,pages=pages)
    book.save()
    # return render(request,"book/createbook.html")
    return redirect("getdetailsmodel")

def getDetailsModel(request):
    book=bookModel.objects.all()
    context = {}
    context["book"] = book
    return render(request,"book/datashowing.html",context)


