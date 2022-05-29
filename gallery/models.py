from tkinter import CASCADE
from django.db import models
from django.forms import CharField
import pyperclip

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=80, default = 'wepukhulu')

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()
        
class Location(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

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


    @classmethod
    def search_image(cls,search_category):
        images = cls.objects.filter(category__name__icontains=search_category)
        return images

    @classmethod
    def filter_by_location(cls,location):
        return cls.objects.filter(location__name__icontains=location)

    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_img_by_id(cls, id):
        image = cls.objects.get(id = id)
        pyperclip.copy(image.image.url)