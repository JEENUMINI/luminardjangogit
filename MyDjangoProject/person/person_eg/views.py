from django.shortcuts import render,redirect
from person_eg.models import Person
from person_eg.forms import PersonCreateForm

# Create your views here.
def personDetails(request):
    form=PersonCreateForm()
    context={}
    context["form"]=form
    if(request.method=='POST'):
        form=PersonCreateForm(request.POST)
        if(form.is_valid()):
            person_name=form.cleaned_data.get("person_name")
            age=form.cleaned_data.get("age")
            salary=form.cleaned_data.get("salary")
            designation =form.cleaned_data.get("designation")
            person = Person(person_name=person_name, age=age, salary=salary, designation=designation)
            person.save()
            return redirect("getpersons")
    return render(request,"person_eg/person_eg.html",context)



def getPersons(request):
    persons=Person.objects.all()
    context={}
    context["persons"]=persons
    return render(request,"person_eg/listperson.html",context)
