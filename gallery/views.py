from django.http import HttpResponse
from django.shortcuts import render
from .models import Image,Location,Category

# Create your views here.
def home(request):
    location = Image.location
    image = Image.filter_by_location(location)
    return render(request, 'home.html', {'location':location, 'img':image})
