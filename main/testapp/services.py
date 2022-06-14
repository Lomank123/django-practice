from testapp.repositories import ItemRepository, CommentRepository, CategoryRepository


class HomeViewService:

    def _build_context(self, items, recent_comment_items):
        return {
            'items': items,
            'recent_comment_items': recent_comment_items,
        }

    def execute(self):
        recent_comments = CommentRepository.get_recent_comments(subquery=True)
        context = {
            'items': ItemRepository.get_items_with_related(),
            'recent_comment_items': ItemRepository.get_recent_comment_items(recent_comments),
            'avg': ItemRepository.get_avg_amount_items(),
            'min_max': ItemRepository.get_min_max_amount_items(),
            'max_avg_diff': ItemRepository.get_avg_max_amount_diff(),
            'categories_with_items_count': CategoryRepository.get_categories_with_items_count(),
            'above_below_20': CategoryRepository.get_categories_with_items_price_above_below_20(),
            'top_3_categories_by_item_count': CategoryRepository.get_top_3_categories_by_amount_items(),
            'has_tag': ItemRepository.has_tag(1, 1),
            'item_tag_info': ItemRepository.get_item_tags_info(1),
        }

        return context
