from django.db import models

# Create your models here.
class Trainer(models.Model):
    name=models.CharField(max_length=150,unique=True)
    age=models.IntegerField()
    total=models.IntegerField()
    course=models.CharField(max_length=150)

    def __str__(self):
        return self.name