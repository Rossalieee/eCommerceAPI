from django.urls import include, path
from rest_framework import routers

from orders.views import ProductViewSet, OrderViewSet, MostOrderedProductsView


router_api = routers.SimpleRouter()
router_api.register(r'products', ProductViewSet, basename='product')
router_api.register(r'orders', OrderViewSet, basename='order')


api_urls = [
    path('', include(router_api.urls)),
    path('products-stats/', MostOrderedProductsView.as_view())
]

