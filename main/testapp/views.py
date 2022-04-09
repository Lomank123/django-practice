from django.shortcuts import render
from django.views.generic.base import TemplateView
from testapp.models import Category, Tag, Item


class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        items = Item.objects.all()
        categories = Category.objects.all()
        tags = Tag.objects.all()
        context["items"] = items
        context["categories"] = categories
        context["tags"] = tags
        return context
    
