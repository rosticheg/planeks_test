from django.test import TestCase, Client

from .models import Schema
from django.contrib.auth.models import User


class FakeCSVTestCase(TestCase):
    def setUp(self):
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        test_user1.save()

        test_schema = Schema.objects.create(title="test1", user=test_user1, file_name="test1.csv")
        test_schema.save()


    def test_schema(self):
        schema1 = Schema.objects.get(id=1)
        self.assertEqual(schema1.title, "test1")
        self.assertEqual(schema1.file_name, "test1.csv")


    def test_check_scheme(self):
        response = self.client.get('/check_scheme/?id=1')
        self.assertTemplateUsed(response=response, template_name='csv_gen/check_scheme.html')


