from datetime import timedelta

from django.utils import timezone
from django.db.models import Exists, F, OuterRef, Avg, Count, Max, Min, FloatField, Q

from testapp.decorators import query_debugger
from testapp.models import Category, Comment, Item


class ItemRepository:

    @staticmethod
    @query_debugger
    def get_items_with_related():
        items = (
            Item.objects
            .all()
            .select_related('category')  # 1 query
            .prefetch_related('tag', 'comment_set', 'comment_set__user')    # 3 queries
        )
        print(items)
        return items

    @staticmethod
    @query_debugger
    def get_item_tags_info(item_id):
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

    @staticmethod
    @query_debugger
    def has_tag(item_id, tag_id):
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

    @staticmethod
    @query_debugger
    def get_recent_comment_items(recent_comments):
        """
        Return Items with additional field called 'recent_comment' which
        shows whether item has comment within 1 day.
        'recent_comment' should be a queryset with OuterRef('pk') to Item.
        """
        # Exists returns bool value
        # Only 1 query here
        items = Item.objects.annotate(recent_comment=Exists(recent_comments))
        print(items)
        return items

    @staticmethod
    @query_debugger
    def get_avg_amount_items():
        """
        Return average amount among all items.
        """
        result = Item.objects.all().aggregate(avg_amount=Avg('amount'))
        print(result)
        return result

    @staticmethod
    @query_debugger
    def get_min_max_amount_items():
        """
        Return min and max amount among all items.
        """
        min_amount = Min('amount')
        max_amount = Max('amount')
        result = Item.objects.all().aggregate(min_amount=min_amount, max_amount=max_amount)
        print(result)
        return result

    @staticmethod
    @query_debugger
    def get_avg_max_amount_diff():
        """
        Difference between max and avg amount.
        """
        avg_amount = Avg('amount')
        max_amount = Max('amount', output_field=FloatField())   # Because avg will be float
        diff = max_amount - avg_amount
        result = Item.objects.aggregate(amount_diff=diff)
        print(result)
        return result


class CategoryRepository:

    @staticmethod
    @query_debugger
    def get_categories_with_items_count():
        """
        Return categories with num_items attr.
        """
        result = Category.objects.annotate(num_items=Count('item'))
        print(result)
        return result

    @staticmethod
    @query_debugger
    def get_categories_with_items_price_above_below_20():
        """
        Categories with 2 additional attrs: number of items where price is above 20 and below 20.
        """
        above_20 = Count('item', filter=Q(item__price__gt=20))
        below_20 = Count('item', filter=Q(item__price__lte=20))
        result = Category.objects.annotate(above_20=above_20).annotate(below_20=below_20)
        print(result)
        return result

    @staticmethod
    @query_debugger
    def get_top_3_categories_by_amount_items():
        """
        Top 3 Categories ordered by amount of items.
        """
        result = Category.objects.annotate(num_items=Count('item')).order_by('-num_items')[:3]
        print(result)
        return result


class CommentRepository:

    @staticmethod
    def get_recent_comments(subquery=False, item_id=None):
        """
        Return item's comments within 1 day. If subquery is True it return
        queryset which contains a reference to an outer query.
        """
        one_day_ago = timezone.now() - timedelta(days=1)
        item = item_id
        if subquery:
            item = OuterRef('pk')
        elif not subquery and item is None:
            raise AttributeError("If subquery is False you must specify item_id.")
        comments = Comment.objects.filter(
            item=item,
            creation_date__gte=one_day_ago,
        )
        if not subquery:
            print(comments)
        return comments
