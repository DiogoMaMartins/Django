from django.db import models

# Create your models here.

class Book(models.Model):
	name = models.CharField( max_length=40)
	numero = models.IntegerField()
	isDpne = models.BooleanField()
	