from os import name
from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.
class LocationTestClass(TestCase):
    '''
    Test class to test the behavior of the location class
    '''

    # Set up method
    def setUp(self):
        # Creating a new location and saving it
        self.new_location = Location(name = 'testing')
        self.new_location.save_location()



    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_location,Location))
    
    def test_save_location(self):
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

class CategoryTestClass(TestCase):
    '''
    Test class to test the behavior of the category class
    '''
    # Set up method
    def setUp(self):
        # Creating a new category and saving it
        self.new_category = Category(name = 'testing')
        self.new_category.save_category()

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_category,Category))

    def test_save_category(self):
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

class ImageTestClass(TestCase):
    '''
    Test class to test the behavior of the image class
    '''
    # Set up method
    def setUp(self):
        # Creating a new image and saving it
        self.new_image= Image(name = 'car', description ='A really cool car')
        self.new_image.save_image()

    # Creating a new location and saving it
        self.new_location = Location(name = 'testing')
        self.new_location.save_location()

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

    def test_save_image(self):
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)


    

