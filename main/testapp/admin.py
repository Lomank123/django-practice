from django.contrib import admin
from testapp.models import Category, Tag, Item, Comment


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Item)
admin.site.register(Comment)
