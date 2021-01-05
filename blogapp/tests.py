from django.test import TestCase, Client
from bs4 import BeautifulSoup
from  .models import Post
from django.utils import timezone
from django.contrib.auth.models import User

# Create your tests here.
def create_post(title, content, author):
    post_ = Post.objects.create(
        title= title,
        content= content,
        created=timezone.now(),
        author=author,
    )
    return post_

class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.author_000 = User.objects.create(username="tester", password='nopassword')

    def test_post_list(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title

        self.assertEqual(title.text, 'Kelly Blog')

        navbar = soup.find('div', id='navbar')
        self.assertIn("Kelly's Note", navbar.text)
        self.assertIn("About", navbar.text)

        self.assertEqual(Post.objects.count(), 0)
#        self.assertIn("Empty Post yet", soup.body.text)
        create_post("first Post", "Hello world", self.author_000)

#    def test_post_detail(self):
