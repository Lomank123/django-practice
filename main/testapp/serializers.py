from rest_framework import serializers
from testapp.models import Category, Tag, Item


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tag = TagSerializer(many=True)

    class Meta:
        model = Item
        fields = '__all__'