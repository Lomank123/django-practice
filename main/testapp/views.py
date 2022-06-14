import requests
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView

from testapp import consts
from testapp.decorators import query_debugger
from testapp.models import Category, Comment, Item, Tag
from testapp.services import HomeViewService


class HomeView(TemplateView):
    template_name = 'testapp/home.html'

    def get(self, request):
        # Cache example - Delayed request
        # If you use cache then for the first time it'll take ~2 secs to get response.
        # After refreshing the page it'll take just ~40ms because of cache.
        request = requests.get(consts.DELAY_URL)
        request.raise_for_status()
        print(request.json())
        return super().get(request=request)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        home_view_context = HomeViewService().execute()
        context.update(home_view_context)
        return context

    @query_debugger
    def has_tag(self, item_id, tag_id):
        """
        Return True if item has certain tag, otherwise False.
        """
        # Recommended (1 query)
        # Cannot use .contains() here after .values_list()
        item_tags = Item.objects.filter(id=item_id).values_list('tag', flat=True)
        has_tag = tag_id in item_tags
        return has_tag
        # Not recommended (2 queries)
        # item = Item.objects.get(id=item_id)
        # return tag_id in item.tag.all().values_list("id", flat=True)

    @query_debugger
    def get_item_tags_info(self, item_id):
        """
        Return names of item's related tags and their count.
        """
        # Recommended (2 queries)
        tags_names = Item.objects.filter(id=item_id).annotate(name1=F('tag__name')).values("name1")
        data = {
            "count": tags_names.count(),
            "tags": list(tags_names)
        }
        return data
        # Not recommended (3 queries)
        # item2 = Item.objects.get(id=1)
        # data = {
        #     "count": item2.tag.count(),
        #     "tags": list(item2.tag.values("name"))
        # }


class ItemDetailView(TemplateView):
    template_name = 'testapp/item_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Item.objects.select_related('category')
        item = get_object_or_404(queryset, pk=self.kwargs["pk"])
        context["item"] = item
        return context
