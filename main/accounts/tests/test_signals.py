import logging
from unittest.mock import patch

from accounts.models import CustomUser, UserProfile
from accounts.signals import new_sign_up
from accounts.views import AccountsSignupView
from django.db.models.signals import post_save
from django.test import TestCase


logging.disable(logging.CRITICAL)


class SignalsTestCase(TestCase):

    @patch('accounts.signals.new_sign_up.send')
    def test_new_sign_up(self, mock):
        header = {"HTTP_USER_AGENT": ""}
        data = {
            "username": "testuser3",
            "password1": "123123123Aa",
            "password2": "123123123Aa"
        }
        self.client.post(path='/auth/signup/', data=data, **header)
        self.assertEqual(mock.call_count, 1)
        self.assertEqual(mock.call_args[1]["new_user"].username, data["username"])


class SignalReceiversTestCase(TestCase):

    def setUp(self):
        self.user1 = CustomUser.objects.create(username="user1", password="123123123Aa")

    def tearDown(self):
        self.user1.delete()

    # It won't work without autospec=True
    # autospec - All attributes of the mock will also have the spec of the corresponding
    # attribute of the object being replaced.
    @patch('accounts.signals.update_profile', autospec=True)
    def test_create_profile(self, mock):
        post_save.connect(mock, sender=CustomUser, dispatch_uid='test_create_profile')
        CustomUser.objects.create(username="testuser2", password="123123123Aa")
        # Check for receiver calls
        self.assertEqual(mock.call_count, 1)
        self.assertTrue(mock.call_args[1]['created'])
        # Check for new objects
        self.assertEqual(CustomUser.objects.count(), 2)
        self.assertEqual(UserProfile.objects.count(), 2)

    @patch('accounts.signals.update_profile', autospec=True)
    def test_update_profile(self, mock):
        post_save.connect(mock, sender=CustomUser, dispatch_uid='test_update_profile')
        self.user1.email = "asv@gmail.com"
        self.user1.save()
        # Check for receiver calls
        self.assertEqual(mock.call_count, 1)
        self.assertFalse(mock.call_args[1]['created'])
        # Check for new objects
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(UserProfile.objects.count(), 1)

    @patch('accounts.signals.notify_new_sign_up', autospec=True)
    def test_notify_new_sign_up(self, mock):
        new_sign_up.connect(mock, sender=AccountsSignupView)
        header = {"HTTP_USER_AGENT": ""}
        data = {
            "username": "testuser3",
            "password1": "123123123Aa",
            "password2": "123123123Aa",
        }
        self.client.post(path='/auth/signup/', data=data, **header)
        self.assertEqual(mock.call_count, 1)
        self.assertEqual(mock.call_args[1]["new_user"].username, data["username"])
        self.assertEqual(CustomUser.objects.count(), 2)
