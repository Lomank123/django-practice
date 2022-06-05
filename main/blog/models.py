from django.db import models
from django.contrib.auth import get_user_model


class BlogPost(models.Model):
    title = models.CharField(max_length=120, verbose_name="Title")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="Author")
    text = models.TextField(max_length=2000, verbose_name="Text")
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")


class BlogComment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="User")
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, verbose_name="Post")
    text = models.CharField(max_length=400, verbose_name="Text")
