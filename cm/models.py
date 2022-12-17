from django.db import models
class student(models.Model):
    username=models.CharField(max_length=40)
    age=models.IntegerField()
    gender=models.CharField(max_length=40)
    phone=models.IntegerField()
    email=models.IntegerField()

class Meta:
    db_table='student'

# Create your models here.
