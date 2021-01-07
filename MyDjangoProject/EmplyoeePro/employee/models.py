from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_name=models.CharField(max_length=150)
    age=models.IntegerField()
    salary=models.IntegerField()
    designation=models.CharField(max_length=150)

    def __str__(self):
        return self.employee_name
