from django.db import models
from django.utils.translation import gettext_lazy as text
from . import Category


# enum
class ProductUnit(models.TextChoices):
    PIECE = "p", text("/cái")
    GRAM = "g", text("/gram")
    KILOGRAM = "kg", text("/Kg")


# custom Manager class, allow custom method at “table-level” 
class ProductManager(models.Manager):
    # custom create method
    def create_product(self, name: str, description: str, price: int, unit: ProductUnit, quantity: int):
        product = self.create(
            name=name,
            price=price,
            unit=unit,
            description=description,
            quantity=quantity,
        )
        # do something with product
        return product

    def count_by_category(self, category: Category):
        return self.get_queryset().filter(categories=category).count()

class Product(models.Model):
    name = models.CharField("Tên hàng hóa", max_length=20)
    price = models.IntegerField("Đơn giá")
    unit = models.CharField("Đơn vị",
        max_length=5,
        choices=ProductUnit, 
        default=ProductUnit.PIECE
    )
    description = models.CharField("Mô tả", max_length=50, null=True, blank=True)
    quantity = models.IntegerField("Số lượng", default=0)
    categories = models.ManyToManyField(Category)

    # custom Manager class
    objects = ProductManager()

    def __str__(self) -> str:
        return self.name