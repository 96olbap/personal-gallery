from tkinter import CASCADE
from django.db import models
from django.forms import CharField
import pyperclip
from cloudinary.models import CloudinaryField

# Create your models here.

class Category(models.Model):
    '''
    Category class to create instances of category objects
    '''
    name = models.CharField(max_length=80, default = 'wepukhulu')

    def __str__(self):
        return self.name

    def save_category(self):
        '''
        save_category method to save a category into the db
        '''
        self.save()

    @classmethod
    def delete_category(cls, id):
        '''
        delete_category method to delete a category object
        '''
        cls.objects.filter(id=id).delete()

    @classmethod
    def update_category(cls,id):
        '''
        update_category method to update a category object
        '''
        return cls.objects.get(id=id)
        
class Location(models.Model):
    '''
    Location class to create instances of location objects
    '''
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    def save_location(self):
        '''
        save_location method to save a location into the db
        '''
        self.save()
    
    @classmethod
    def delete_location(cls, id):
        '''
        delete_location method to delete an location object
        '''
        cls.objects.filter(id=id).delete()

    @classmethod
    def update_location(cls,id):
        '''
        update_location method to update a location object
        '''
        return cls.objects.get(id=id)

class Image(models.Model):
    '''
    Image class to create instances of image objects
    '''
    image = CloudinaryField('image')
    name = models.CharField(max_length=100)
    description = models.TextField(max_length = 50,blank = True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def save_image(self):
        '''
        save_image method to save an image into the db
        '''
        self.save()
    class Meta:
        ordering = ['uploaded_at']

    @classmethod
    def search_image(cls,search_category):
        '''
        search_image method to search for an image based on the category
        '''
        images = cls.objects.filter(category__name__icontains=search_category)
        return images

    @classmethod
    def filter_by_location(cls,location):
        '''
        filter_by_location method to query the db for all image objects with a specific location
        '''
        return cls.objects.filter(location__name__icontains=location)

    @classmethod
    def all_images(cls):
        '''
        all_images method to query the db for all image objects
        '''
        images = cls.objects.all()
        return images

    @classmethod
    def get_img_by_id(cls, id):
        '''
        get_img_by_id method to query the db for an image object with a specific id
        '''
        image = cls.objects.get(id = id)
        return image

    @classmethod
    def update_image(cls, id):
        '''
        update_image method to update an image object
        '''
        image = cls.objects.get(id = id)
        return image

    @classmethod
    def delete_image(cls, id):
        '''
        delete_image method to delete an image object
        '''
        cls.objects.filter(id=id).delete()
