from testapp.models import Item


def item_count(request):
    """
    Simple context processor that adds count of Items.
    """
    all_items_count = Item.objects.all().count()
    return {
        "all_items_count": all_items_count,
    }
