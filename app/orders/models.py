from django.contrib.auth import get_user_model
from django.db import models
from e_commerce.abstract_models import BaseModel
from django_advance_thumbnail import AdvanceThumbnailField
from django.core.validators import FileExtensionValidator

UserModel = get_user_model()


class ProductCategory(BaseModel):
    name = models.CharField(max_length=120)

    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return f'{self.name}'


class Product(BaseModel):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=9)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    photo = models.FileField(upload_to='photos/', validators=[FileExtensionValidator(['jpg', 'png'])])
    thumbnail = AdvanceThumbnailField(source_field='photo', upload_to='thumbnails/', null=True, blank=True, size=(200, 200))


class Order(BaseModel):
    customer = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='orders')
    shipping_address = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True, null=True)
    payment_date = models.DateTimeField(null=True)
    products = models.ManyToManyField(Product, related_name='orders')

    @property
    def products_count(self):
        return self.products.count()

    @property
    def total_price(self):
        total = 0
        for product in self.products.all():
            total += product.price
        return total

