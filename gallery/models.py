from tkinter import CASCADE
from django.db import models
from django.forms import CharField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=80, default = 'wepukhulu')

    def __str__(self):
        return self.name
        
class Location(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to = 'uploads/', default='Wepukhulu')
    name = models.CharField(max_length=100)
    description = models.TextField(max_length = 50,blank = True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()
    class Meta:
        ordering = ['uploaded_at']

    def delete_image(self):
        self.delete()

    def get_image_by_id(self,id):
        return self.objects.get(id=id)

    @classmethod
    def search_image(cls,category):
        return cls.objects.filter(category__name__icontains=category)

    @classmethod
    def filter_by_location(cls,location):
        return cls.objects.filter(location__name__icontains=location)