from django.db import models

# Create your models here.

class bookCreateModel(models.Model):
    bookname=models.CharField(max_length=150)
    price=models.IntegerField()
    pages=models.IntegerField()
    author=models.CharField(max_length=150)

    def __str__(self):
        return self.bookname

