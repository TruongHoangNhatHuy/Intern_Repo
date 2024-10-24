from django.db import models
from . import Order, Product


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField("Số lượng", default=1)
    price = models.IntegerField("Đơn giá")

    def __str__(self) -> str:
        return self.id