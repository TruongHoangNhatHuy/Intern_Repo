from django.db import models
from . import User, Product, OrderProduct
from django.utils.translation import gettext_lazy as text
from datetime import datetime


# enum
class OrderStatus(models.TextChoices):
    INCOMPLETE = "incomplete", text("Chưa đặt")
    DOING = "doing", text("Đang thực hiện")
    PAID = "paid", text("Đã thanh toán")
    DONE = "done", text("Đã hoàn thành")


class OrderManager(models.Manager):
    def create_order(self, user: User, ship_address: str):
        order = self.create(
            user = user,
            date = datetime.now(),
            ship_address = ship_address,
            status = "incomplete"
        )
        # do something with product
        return order


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through="OrderProduct")
    date = models.DateTimeField("Thời gian tạo")
    ship_address = models.CharField("Địa chỉ nhận", max_length=50)
    status = models.CharField("Trạng thái",
        max_length=10,
        choices=OrderStatus,
        default=OrderStatus.INCOMPLETE
    )

    def __str__(self) -> str:
        return self.id
    
    def add_product(self, order_product: OrderProduct):
        self.products.add(order_product)

    def remove_product(self, order_product: OrderProduct):
        self.products.remove(order_product)