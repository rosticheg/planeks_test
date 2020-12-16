from django.test import TestCase, Client

from .models import Schema
from django.contrib.auth.models import User


class FakeCSVTestCase(TestCase):
    def setUp(self):
        self.test_user1 = User.objects.create_user(username='testuser1', password='12345')
        self.test_user1.save()
        self.client = Client()
        logged_in = self.client.login(username='testuser1', password='12345')      

        self.test_schema = Schema.objects.create(title="test1", user=self.test_user1, file_name="test1.csv")
        self.test_schema.save()


    def test_schema(self):
        schema1 = Schema.objects.get(id=1)
        self.assertEqual(schema1.title, "test1")
        self.assertEqual(schema1.file_name, "test1.csv")


    def test_check_scheme(self):
        response = self.client.get('/check_scheme/?id=1')
        self.assertTemplateUsed(response=response, template_name='csv_gen/check_scheme.html')


    def test_generate_function(self):

        # All params good
        my_data = {'schema_name': ['test'], 'rows_number': ['10'], 'separ': [';'], 'name0': ['col'], 'typ0': ['1'], 'order0': ['1']}
        response = self.client.post('/generate/', my_data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response=response, template_name='csv_gen/my_schemas.html')

        # Missing one param
        my_data = {'schema_name': ['test'], 'rows_number': ['10'], 'separ': [';'], 'typ0': ['1'], 'order0': ['1']}
        response = self.client.post('/generate/', my_data)

        self.assertTemplateUsed(response=response, template_name='csv_gen/new_schema.html')




