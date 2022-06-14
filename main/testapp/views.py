import requests
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView

from testapp import consts
from testapp.services import HomeViewService
from testapp.models import Item


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


class ItemDetailView(TemplateView):
    template_name = 'testapp/item_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Item.objects.select_related('category')
        item = get_object_or_404(queryset, pk=self.kwargs["pk"])
        context["item"] = item
        return context
