from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=120, verbose_name="Name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"
        ordering = ['-id']


class Tag(models.Model):
    name = models.CharField(max_length=120, verbose_name="Name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Tags"
        verbose_name = "Tag"
        ordering = ['-id']


class Item(models.Model):
    name = models.CharField(max_length=120, verbose_name="Name")
    publication_date = models.DateTimeField(auto_now_add=True, verbose_name="Publication date")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Update date")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category")
    tag = models.ManyToManyField(Tag, verbose_name="Tag")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Items"
        verbose_name = "Item"
        ordering = ['-id']


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    item = models.ForeignKey(Item, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Item")
    text = models.CharField(max_length=360, verbose_name="Text")
    publication_date = models.DateTimeField(auto_now_add=True, verbose_name="Published in")

    class Meta:
        verbose_name_plural = "Comments"
        verbose_name = "Comment"
        ordering = ['-id']


class Employee(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='people', verbose_name='Boss')
    name = models.CharField(max_length=120, verbose_name='Name')
    position = models.CharField(max_length=120, verbose_name='Position')

    class MPTTMeta:
        order_instertion_by = ['name']
