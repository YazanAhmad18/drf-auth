from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Airplane
from django.urls import reverse
from rest_framework.test import APITestCase


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

class APITest(APITestCase):
        def test_auth_list(self):
            response = self.client.get(reverse('airplane_list'))
            self.assertEqual(response.status_code, 401)