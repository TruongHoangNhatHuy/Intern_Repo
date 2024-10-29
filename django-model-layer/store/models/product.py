from django.db import models
from django.db.models import F, Q, Case, When, Value, Count
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

    # def count_by_category(self, category: Category):
    #     return self.get_queryset().filter(categories=category).count()
    def count_by_category(self):
        for c in Category.objects.all():
            print(c.name + ":\t", self.get_queryset().filter(categories=c).count())
    
    def stock_status(self):
        return self.annotate(
            status=Case(
                When(quantity__lt=10, then=Value("Low")),
                When(quantity__in=range(10,20), then=Value("Enough")),
                When(quantity__gte=20, then=Value("Sufficient")),
                default=Value("Unknown")
            )
        ).values_list("name", "status")


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
    
    def restock(self, addCount: int):
        product = Product.objects.filter(pk=self.pk)
        num_rows_updated = product.update(quantity=F("quantity") + addCount) # F() code will execute on DB
        self.refresh_from_db() # sync with DB
        return num_rows_updated
        # equivalent:
        product = Product.objects.get(self.pk)
        product.quantity = F("quantity") + addCount
        product.save()
        product.refresh_from_db()