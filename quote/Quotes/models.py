from django.db import models
from django.contrib.postgres.fields import ArrayField

class Quote(models.Model):
    tags = ArrayField(models.CharField(max_length=100), blank=True)
    author=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)

class author(models.Model):
    fullname=models.CharField(max_length=100)
    born_date=models.CharField(max_length=90)
    born_location=models.CharField(max_length=200)
    description=models.CharField(max_length=1800)