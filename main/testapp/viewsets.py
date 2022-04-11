from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from testapp.models import Category, Tag, Item
from testapp.serializers import CategorySerializer, TagSerializer, ItemSerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = (AllowAny, )

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset


class TagViewSet(ModelViewSet):
    serializer_class = TagSerializer
    permission_classes = (AllowAny, )

    def get_queryset(self):
        queryset = Tag.objects.all()
        return queryset


class ItemViewSet(ModelViewSet):
    serializer_class = ItemSerializer
    permission_classes = (AllowAny, )

    def get_queryset(self):
        queryset = Item.objects.select_related('category').prefetch_related('tag')
        return queryset
