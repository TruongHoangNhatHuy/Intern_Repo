from django.db import models
from . import Category


class Product(models.Model):
    name = models.CharField("Tên hàng hóa", max_length=20)
    price = models.IntegerField("Đơn giá")
    unit = models.CharField("Đơn vị",
        max_length=5,
        choices={
            "p": "/cái",
            "g": "/gram",
            "kg": "/Kgram",
        }, 
        default="p"
    )
    description = models.CharField("Mô tả", max_length=50, null=True, blank=True)
    quantity = models.IntegerField("Số lượng", default=0)
    categories = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return self.name