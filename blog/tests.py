from django.test import TestCase
from django.urls import reverse
from .models import Post, Category
from django.contrib.auth.models import User


class PostModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user', password='password')
        self.category = Category.objects.create(name='category')
        self.post = Post.objects.create(title='post', content='content', user=self.user, category=self.category)

    def test_post_creation(self):
        self.assertEquals(self.post.title, 'post')
        self.assertEquals(self.post.content, 'content')
        self.assertEquals(self.post.category.name, 'category')
        self.assertEquals(self.post.user.username, 'user')


class PostViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user', password='password')
        self.category = Category.objects.create(name='category')
        self.post = Post.objects.create(title='post', content='content', user=self.user, category=self.category)

    def test_home(self):
        # import ipdb;
        # ipdb.set_trace()
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        # self.assertEqual(response, 'post')

    def test_create_post_view(self):
        self.client.login(username='user', password='password')
        url = reverse('blog:create_post')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_edit_post_view(self):
        self.client.login(username='user', password='password')
        url = reverse('blog:edit_post', args=[self.post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_post_view(self):
        self.client.login(username='user', password='password')
        url = reverse('blog:view_post', args=[self.post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.content.decode().find('title'), -1)
        self.assertNotEqual(response.content.decode().find('content'), -1)

    def test_delete_post_view(self):
        self.client.login(username='user', password='password')
        url = reverse('blog:delete_post', args=[self.post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
