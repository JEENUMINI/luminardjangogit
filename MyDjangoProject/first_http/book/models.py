from django.db import models

# Create your models here.
class bookModel(models.Model):
    name=models.CharField(max_length=120)
    price=models.IntegerField()
    pages=models.IntegerField()

    def __str__(self):
        return self.name

