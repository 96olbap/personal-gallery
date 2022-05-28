from os import name
from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.
class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        # Creating a new location and saving it
        self.new_location = Location(name = 'testing')
        self.new_location.save()



    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_location,Location))

class CategoryTestClass(TestCase):
    # Set up method
    def setUp(self):
        # Creating a new category and saving it
        self.new_category = Category(name = 'testing')
        self.new_category.save()

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_category,Category))

class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        # Creating a new image and saving it
        self.new_image= Image(name = 'car', description ='A really cool car')
        self.new_image.save_image()

    # Creating a new location and saving it
        self.new_location = Location(name = 'testing')
        self.new_location.save()

    # Creating a new category and saving it
        self.new_category = Category(name = 'testing')
        self.new_category.save()

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

    # def test_get_image_by_category(self):


    

