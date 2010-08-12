from django.test import TestCase
from django.test import Client

class BlogViewsTest(TestCase) :
	def test_visit_root(self):
		client = Client()
		response = client.get('/')
		self.assertUnless(response.status_code < 400)