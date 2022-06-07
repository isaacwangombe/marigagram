from django.test import TestCase
from .models import Profile, Comment, Post

class CommentTest(TestCase):
  
    def setUp(self):
        self.new_category = Profile(name='testing')
        self.new_category.save_category()
        
        self.new_location = Comment(city='Nairobi', country='Kenya')
        self.new_location.save_location()
        
        self.new_picture = Comment(image_link='Comment/picture.jpeg', title='Image title', description='sth random', category=self.new_category, location=self.new_location)
        self.new_picture.save_image()
        self.another_picture = Comment(image_link='Comment/photo.jpg', title='Another title', description='sth else more random', category=self.new_category, location=self.new_location)
        self.another_picture.save_image()

    def tearDown(self):
        Profile.objects.all().delete()
        Comment.objects.all().delete()
        Comment.objects.all().delete()

    def test_instances(self):
        self.assertTrue(isinstance(self.new_picture,Comment))
        self.assertTrue(isinstance(self.new_category, Profile))
        self.assertTrue(isinstance(self.new_location, Comment))

    def test_save_image(self):
        self.assertTrue(len(Comment.objects.all()) == 2)

    def test_delete_image(self):
        self.new_picture.delete_image()
        self.assertTrue(len(Comment.objects.all()) == 1)

    def test_update_image(self):
        update_test = self.new_picture.update_image('Comment/updated.png')
        self.assertEqual(update_test.image_link, 'Comment/updated.png')

    def test_get_all(self):
        pictures = Comment.get_all()
        # print(pictures)

    def test_get_image_by_id(self):
        obtained_image = Comment.get_image_by_id(self.another_picture.id)
        # print(obtained_image.title)

        obtained_image = Comment.search_image(self.new_picture.category)
        print(obtained_image) 

    def test_filter_by_location(self):
        obtained_image = Comment.filter_by_location(self.another_picture.location)
        print(obtained_image)



class CategoryTest(TestCase):
    def setUp(self):
        self.new_category = Profile(name='categoryA')
        self.new_category.save_category()

    def tearDown(self):
        Profile.objects.all().delete()

    def test_save_category(self):
        self.assertTrue(len(Profile.objects.all()) == 1)     

    def test_delete_category(self):
        self.new_category.save_category()
        self.new_category.delete_category()
        self.assertTrue(len(Profile.objects.all()) == 0)    

    def test_update_category(self):
        update_cat = Profile.update_category('categoryA', 'CategoryB')
        self.assertEqual(update_cat.name, 'CategoryB')




class LocationTest(TestCase):
    def setUp(self):
        self.new_location = Comment(city='Nairobi')
        self.new_location.save_location()

    def test_save_location(self):
        self.assertTrue(len(Comment.objects.all()) == 1)     

    def test_delete_location(self):
        self.new_location.save_location()
        self.new_location.delete_location()
        self.assertTrue(len(Comment.objects.all()) == 0)

    def test_update_location(self):
        update_locale = Comment.update_location('unknown', 'Mombasa')
        self.assertEqual(update_locale.city, 'Mombasa')

    def test_get_all(self):
        Comment = Comment.get_all()
        print(Comment)