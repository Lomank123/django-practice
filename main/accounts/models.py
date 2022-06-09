from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    about = models.TextField(max_length=900, null=True, blank=True, verbose_name="About")

    def __str__(self):
        return self.user.username
