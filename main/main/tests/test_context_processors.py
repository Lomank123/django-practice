from unittest.mock import Mock

from django.test import TestCase
from main.context_processors.custom import item_count
from testapp.models import Category, Item


class CustomContextProcessorTestCase(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Category 1")
        self.item1 = Item.objects.create(name="Item 1", category=self.category)
        self.item2 = Item.objects.create(name="Item 2", category=self.category)

    def test_item_count(self):
        request = Mock()
        res = item_count(request)
        self.assertEqual(res, {"all_items_count": 2})
