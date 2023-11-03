from datetime import timedelta

from django.db.models import Count, Q
from django.utils import timezone
from rest_framework import viewsets, mixins, status, views
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer, MostOrderedProductsSerializer
from .permissions import IsSellerOrReadOnly, HasCustomerPermission, HasSellerPermission


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsSellerOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'category', 'price', 'description']
    ordering_fields = ['name', 'category', 'price']


class OrderViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [HasCustomerPermission]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        address = request.data.get('address')
        payment_date = timezone.now() + timedelta(days=5)
        user = request.user

        serializer.validated_data['shipping_address'] = f"{first_name} {last_name}, {address}"
        serializer.validated_data['payment_date'] = payment_date
        serializer.validated_data['customer'] = user

        self.perform_create(serializer)

        if user.email:
            email_subject = 'Order received'
            email_message = 'Thank you! Your order has been received.'
            user.email_user(email_subject, email_message)

        headers = self.get_success_headers(serializer.data)

        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class MostOrderedProductsView(views.APIView):
    serializer_class = MostOrderedProductsSerializer
    permission_classes = [HasSellerPermission]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            start_date = serializer.validated_data['start_date']
            end_date = serializer.validated_data['end_date']
            num_products = serializer.validated_data['num_products']

            most_ordered_products = Product.objects.annotate(
                total_orders=Count('orders', filter=Q(orders__order_date__range=(start_date, end_date)))
            ).order_by('-total_orders')[:num_products]

            response_data = []
            for product in most_ordered_products:
                product_data = ProductSerializer(product).data
                product_data['total_orders'] = product.total_orders
                response_data.append(product_data)

            return Response(response_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
