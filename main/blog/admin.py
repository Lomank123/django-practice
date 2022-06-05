from django.contrib import admin
from blog.models import BlogPost, BlogComment


admin.site.register(BlogPost)
admin.site.register(BlogComment)
