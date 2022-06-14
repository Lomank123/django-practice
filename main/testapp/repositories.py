from datetime import timedelta

from django.utils import timezone
from django.db.models import Exists, F, OuterRef

from testapp.decorators import query_debugger
from testapp.models import Category, Comment, Item, Tag


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


class CategoryRepository:
    pass


class TagRepository:
    pass


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
