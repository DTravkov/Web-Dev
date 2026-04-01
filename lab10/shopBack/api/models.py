from django.db import models

from .utils import get_default_category


class Category(models.Model):
    name = models.CharField(max_length=150, null=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150, null=False)
    price = models.FloatField(null=False)
    description = models.TextField()
    is_active = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=get_default_category, null=False)
    

    def __str__(self):
        return self.name