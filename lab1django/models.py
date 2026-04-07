from django.db import models

# Create your models here.

class Book(models.Model):
    author = models.CharField()
    rating = models.IntegerField()
    title = models.CharField()
    genre = models.CharField()
    publication_date = models.DateField()
