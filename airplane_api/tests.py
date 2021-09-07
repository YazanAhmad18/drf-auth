from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Airplane

# Create your tests here.
class AirplanesTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()
        test_post = Airplane.objects.create(author=testuser1, type='airbus', description='380a' )
        test_post.save()

    def test_blog_content(self):
        post = Airplane.objects.get(id = 1)
        expected_author = f'{post.author}'
        expected_airplanetype = f'{post.type}'
        expected_description = f'{post.description}'
        self.assertEqual(expected_author, 'testuser1')
        self.assertEqual(expected_airplanetype, 'airbus')
        self.assertEqual(expected_description, '380a')