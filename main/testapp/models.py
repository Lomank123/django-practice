from django.db import models


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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category")
    tag = models.ManyToManyField(Tag, verbose_name="Tag")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Items"
        verbose_name = "Item"
        ordering = ['-id']
