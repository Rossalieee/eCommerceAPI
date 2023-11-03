from django.db import models


class UserRole(models.TextChoices):
    CUSTOMER = 'CUSTOMER', 'Customer'
    SELLER = 'SELLER', 'Seller'
