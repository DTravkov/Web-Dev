from django.db import models

from .utils import get_default_category


class ProductCategory(models.Model):
    name = models.CharField(max_length=150, unique=True, null=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150, null=False, default="N/A")
    price = models.FloatField(null=False)
    description = models.TextField(default="N/A")
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_DEFAULT, default=get_default_category, null=False)


    def __str__(self):
        return self.name