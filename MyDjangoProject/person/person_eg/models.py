from django.db import models

# Create your models here.
class Person(models.Model):
    person_name=models.CharField(max_length=150,unique=True)
    age=models.IntegerField()
    salary=models.IntegerField()
    designation=models.CharField(max_length=120)

    def __str__(self):
        return self.person_name

#python manage.py makemigrations
#python manage.py migrate
#CRUD(create retrive update delete)
#ORM
#python manage.py shell
#obj=Book(book_name="half girl friend",price=150,pages=100,author="chethanbhagath")
#obj.save()
#select * from books
#books=book.objects.all()
#select book_name from Book where id=1 in mysql
#book=Book.objects.get(id=1)
#books=Book.objects.filter(price=300)
#fetch all book having price<300
#books=Book.objects.filter(price__lt=300)
#books=Book.objects.filter(price__lte=300)
#books=Book.objects.filter(price__gt=300)
#books=Book.objects.filter(price__gte=300)



