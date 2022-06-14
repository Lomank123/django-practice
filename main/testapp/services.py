from testapp.repositories import ItemRepository, CommentRepository


class HomeViewService:

    def _build_context(self, items, recent_comment_items):
        return {
            'items': items,
            'recent_comment_items': recent_comment_items,
        }

    def execute(self):
        recent_comments = CommentRepository.get_recent_comments(subquery=True)
        recent_comment_items = ItemRepository.get_recent_comment_items(recent_comments)
        items = ItemRepository.get_items_with_related()
        context = self._build_context(items, recent_comment_items)
        return context
