from abc import ABC

from rest_framework import serializers
from .models import Product, Order


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['id', 'thumbnail']


class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.DecimalField(max_digits=9, decimal_places=2, read_only=True)
    products_count = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    address = serializers.CharField(write_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['id', 'order_date', 'payment_date', 'customer', 'shipping_address']

    def create(self, validated_data):
        validated_data.pop('first_name', None)
        validated_data.pop('last_name', None)
        validated_data.pop('address', None)
        return super().create(validated_data)


class MostOrderedProductsSerializer(serializers.Serializer):
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    num_products = serializers.IntegerField()
