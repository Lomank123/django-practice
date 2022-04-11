from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from testapp.models import Category, Tag, Item
from django.shortcuts import get_object_or_404


class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        items = (
            Item.objects
            .all()
            .select_related('category')
            .prefetch_related('tag')
            #.values('name', 'category__name')
        )
        categories = Category.objects.all()
        tags = Tag.objects.all()
        context["items"] = items
        context["categories"] = categories
        context["tags"] = tags
        return context


class ItemDetailView(TemplateView):
    template_name = 'item_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Item.objects.select_related('category')
        item = get_object_or_404(queryset, pk=self.kwargs["pk"])
        #item = Item.objects.filter(id=self.kwargs["pk"]).select_related('category').first()
        context["item"] = item
        return context
