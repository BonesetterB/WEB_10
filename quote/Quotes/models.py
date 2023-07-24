from django.db import models



class author(models.Model):
    fullname=models.CharField(max_length=100)
    born_date=models.CharField(max_length=90)
    born_location=models.CharField(max_length=200)
    description=models.TextField()

class Tag(models.Model):
    name=models.CharField(max_length=50,null=False,unique=True)

class Quote(models.Model):
    quote=models.TextField()
    author=models.ForeignKey(author, on_delete=models.CASCADE,default=None,null=True)
    tags=models.ManyToManyField(Tag)