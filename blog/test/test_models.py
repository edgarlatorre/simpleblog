from simpleblog.blog.models import Post
from datetime import datetime

class PostTest(TestCase) :
	def test_should_make_published_date(self):
		post = Post(title='teste', body='body')
		try :
			post.save()
		except :
			self.fail()
	
	def test_should_make_slug(self):
		post = Post(title='teste slug', body='conteudo', published=datetime.now())
		post.save()
		self.assertTrue(post.slug == 'teste-slug')

class ClientTests(TestCase) :
	client = Client()