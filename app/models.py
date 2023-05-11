from django.db import models

# Create your models here.
class student(models.Model):
    sname=models.CharField(max_length=100,primary_key=True)
    sage=models.IntegerField()
    def __str__(self) -> str:
        return self.sname
