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
        '''
        setup method that will run before every test
        '''
        # Creating a new location and saving it
        self.new_location = Location(name = 'testing')
        self.new_location.save_location()



    # Testing instance
    def test_instance(self):
        '''
        test_instance test case to test for an instance of the location object
        '''
        self.assertTrue(isinstance(self.new_location,Location))
    
    def test_save_location(self):
        '''
        test_save_location test case to test if the location is added to the database
        '''
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

    def test_delete_location(self):
        '''
        test_delete_location test case to test if the location is deleted from the database
        '''
        Location.delete_location(self.new_location.id)
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)

    def test_update_location(self):
        '''
        test_update_location test case to test whether we can access the location object and update it
        '''
        location = Location.update_location(self.new_location.id)
        self.assertEqual(location, self.new_location)

class CategoryTestClass(TestCase):
    '''
    Test class to test the behavior of the category class
    '''
    # Set up method
    def setUp(self):
        '''
        Creating a new category and saving it
        '''
        self.new_category = Category(name = 'testing')
        self.new_category.save_category()

    # Testing instance
    def test_instance(self):
        '''
        test_instance test case to test for an instance of the category object
        '''
        self.assertTrue(isinstance(self.new_category,Category))

    def test_save_category(self):
        '''
        test_save_category test case to test if the category is added to the database
        '''
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        '''
        test_delete_category test case to test if the category is deleted from the database
        '''
        Category.delete_category(self.new_category.id)
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)

    def test_update_category(self):
        '''
        test_update_category test case to test whether we can access the category object and update it
        '''
        category = Category.update_category(self.new_category.id)
        self.assertEqual(category, self.new_category)

class ImageTestClass(TestCase):
    '''
    Test class to test the behavior of the image class
    '''
    # Set up method
    def setUp(self):
        '''
        Creating a new image and saving it
        '''
        self.new_image= Image(name = 'car', description ='A really cool car')
        self.new_image.save_image()

    # Creating a new location and saving it
        self.new_location = Location(name = 'testing')
        self.new_location.save_location()

    # Creating a new category and saving it
        self.new_category = Category(name = 'testing')
        self.new_category.save()

    def tearDown(self):
        '''
        teardown function to delete all created instances used in running the tests
        '''
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    # Testing instance
    def test_instance(self):
        '''
        test_instance test case to test for an instance of the image object
        '''
        self.assertTrue(isinstance(self.new_image,Image))

    def test_save_image(self):
        '''
        test_save_image test case to test if the image is added to the database
        '''
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        '''
        test_delete_image test case to test if the image is deleted from the database
        '''
        Image.delete_image(self.new_image.id)
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)


    def test_get_img_by_id(self):
        '''
        test_get_img_by_id test case to test if the image url is copied
        '''
        image = Image.get_img_by_id(self.new_image.id)
        self.assertEqual(image, self.new_image)
    
    def test_update_image(self):
        '''
        test_update_image test case to test whether we can access the image object and update it
        '''
        image = Image.update_image(self.new_image.id)
        self.assertEqual(image, self.new_image)
        


    

