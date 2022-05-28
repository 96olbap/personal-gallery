from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'uuploads/')
    name = models.CharField(max_length=100)
    description = models.TextField(max_length = 50,blank = True)
    uploaded_at = models.DateTimeField(auto_now_add=True)