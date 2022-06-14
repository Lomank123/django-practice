from django.db import models
from django.contrib.auth import get_user_model


class CustomBaseModel(models.Model):

    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    last_update = models.DateTimeField(auto_now=True, verbose_name="Last update")

    class Meta:
        abstract = True


class Category(CustomBaseModel):
    name = models.CharField(max_length=120, verbose_name="Name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"
        ordering = ['-id']


class Tag(CustomBaseModel):
    name = models.CharField(max_length=120, verbose_name="Name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Tags"
        verbose_name = "Tag"
        ordering = ['-id']


class Item(CustomBaseModel):
    name = models.CharField(max_length=120, verbose_name="Name")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category")
    tag = models.ManyToManyField(Tag, blank=True, verbose_name="Tag")
    amount = models.IntegerField(default=0, verbose_name="Amount")
    price = models.DecimalField(default=0.0, max_digits=7, decimal_places=2, verbose_name="Price")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Items"
        verbose_name = "Item"
        ordering = ['-id']


class Comment(CustomBaseModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="User")
    item = models.ForeignKey(Item, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Item")
    text = models.CharField(max_length=360, verbose_name="Text")

    class Meta:
        verbose_name_plural = "Comments"
        verbose_name = "Comment"
        ordering = ['-id']
