from datetime import timedelta

from django.db.models import Exists, OuterRef
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic.base import TemplateView

from testapp.models import Category, Comment, Employee, Item, Tag


class HomeView(TemplateView):
    template_name = 'testapp/home.html'

    def get_context_data(self, **kwargs):
        # self.create_employees()
        context = super().get_context_data(**kwargs)
        items = (
            Item.objects
            .all()
            .select_related('category')
            .prefetch_related('tag', 'comment_set')
            # .values('name', 'category__name')
        )
        categories = Category.objects.all()
        tags = Tag.objects.all()
        employees = Employee.objects.all()
        context["items"] = items
        context["categories"] = categories
        context["tags"] = tags
        context["employees"] = employees
        # context["recent_comment_items"] = self.get_recent_comment_items()

        return context

    def create_employees(self):
        # Bosses
        for i in range(2):
            boss = Employee.objects.create(name="boss123", position="boss")
            e1 = Employee.objects.create(name="1empl", position="1empl", parent_id=boss.id)
            e2 = Employee.objects.create(name="2empl", position="2empl", parent_id=e1.id)
            e3 = Employee.objects.create(name="3empl", position="3empl", parent_id=e2.id)
            Employee.objects.create(name="4empl", position="4empl", parent_id=e3.id)

    def get_item_queries(self):
        pass

    def get_category_queries(self):
        pass

    def get_tag_queries(self):
        pass

    def get_employees(self):
        pass

    def get_recent_comment_items(self):
        """
        Returns Items with additional field called 'recent_comment' which
        shows whether item has comment within 1 day
        """
        one_day_ago = timezone.now() - timedelta(days=1)
        recent_comments = Comment.objects.filter(
            item=OuterRef('pk'),
            publication_date__gte=one_day_ago,
        )
        # Exists returns bool value
        items = Item.objects.annotate(recent_comment=Exists(recent_comments))
        return items


class ItemDetailView(TemplateView):
    template_name = 'testapp/item_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Item.objects.select_related('category')
        item = get_object_or_404(queryset, pk=self.kwargs["pk"])
        # item = Item.objects.filter(id=self.kwargs["pk"]).select_related('category').first()
        context["item"] = item
        return context
