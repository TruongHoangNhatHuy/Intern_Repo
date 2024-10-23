from django.db import models
from . import User, Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through="OrderProduct")
    date = models.DateTimeField("Thời gian tạo")
    ship_address = models.CharField("Địa chỉ nhận", max_length=50)
    status = models.CharField("Trạng thái",
        max_length=10,
        choices={
            "incomplete": "Chưa đặt",
            "doing": "Đang thực hiện",
            "paid": "Đã thanh toán",
            "done": "Đã hoàn thành",
        },
        default="incomplete"
    )

    def __str__(self) -> str:
        return self.id