from django.urls import path, include
from django.views.decorators.cache import cache_page
from rest_framework.routers import DefaultRouter
from testapp.views import HomeView, ItemDetailView
from testapp.viewsets import CategoryViewSet, TagViewSet, ItemViewSet


router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('tag', TagViewSet, basename='tag')
router.register('item', ItemViewSet, basename='item')

urlpatterns = [
    path('', cache_page(60 * 5)(HomeView.as_view()), name='home'),
    path('<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    # API
    path('api/', include(router.urls)),
]
