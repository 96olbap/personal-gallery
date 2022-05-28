from django.db import models
from django.forms import CharField

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'uploads/', default='Wepukhulu')
    name = models.CharField(max_length=100)
    description = models.TextField(max_length = 50,blank = True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = CharField(max_length= 150)

    def __str__(self):
        return self.name