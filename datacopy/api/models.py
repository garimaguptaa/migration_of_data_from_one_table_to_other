from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=10)
    age = models.IntegerField()


class StudentCopy(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=10)
    age = models.IntegerField()

