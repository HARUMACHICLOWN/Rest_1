from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    annotation = models.TextField(blank=True)
    year = models.DateField()
