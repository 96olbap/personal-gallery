from django.http import HttpResponse
from django.shortcuts import render
from .models import Image,Location,Category

# Create your views here.
def home(request):
    images = Image.all_images()

    print(images)
    return render(request, 'home.html', {'images':images})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_category = request.GET.get("category")
        searched_images = Image.search_image(search_category)
        message = f"{search_category}"

        return render(request, 'search.html', {"message": message, "images": searched_images})

    else:
        message = "You have not searched for any category"
        return render(request, 'search.html', {"message": message})