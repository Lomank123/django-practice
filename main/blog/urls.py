from django.urls import path
from blog.views import BlogPostDetailView


urlpatterns = [
    path('<int:pk>/', BlogPostDetailView.as_view(), name='blog-detail'),
]
