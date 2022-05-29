from django.http import HttpResponse
from django.shortcuts import render
from .models import Image,Location,Category

# Create your views here.
def home(request):
    images = Image.all_images()

    print(images)
    return render(request, 'home.html', {'images':images})
