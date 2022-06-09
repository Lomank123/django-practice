import logging

from accounts.models import CustomUser
from blog.models import BlogPost
from django.contrib.sessions.models import Session
from django.test import TestCase, override_settings


logging.disable(logging.CRITICAL)


class SessionsTestCase(TestCase):

    def setUp(self):
        self.user1 = CustomUser.objects.create(username="user1", password="123123123Aa")
        self.user2 = CustomUser.objects.create(username="user2", password="123123123Aa")
        self.blog_post = BlogPost.objects.create(title="BlogPost1", author=self.user1, text="Text")

    def tearDown(self):
        self.user1.delete()
        self.user2.delete()
        self.blog_post.delete()

    @override_settings(SESSION_ENGINE='django.contrib.sessions.backends.db')
    def test_session(self):
        self.assertEqual(CustomUser.objects.count(), 2)
        self.assertEqual(BlogPost.objects.count(), 1)
        # Issue a GET request.
        self.client.force_login(self.user1)
        header = {"HTTP_USER_AGENT": ""}
        response = self.client.get(f'/blog/{self.blog_post.id}/', **header)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.client.session["num_visits"], 1)
        response2 = self.client.get(f'/blog/{self.blog_post.id}/', **header)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(self.client.session["num_visits"], 2)
        self.assertEqual(Session.objects.count(), 1)
