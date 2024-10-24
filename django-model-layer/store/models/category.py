from django.db import models


class Category(models.Model):
    name = models.CharField("Danh mục", max_length=20)
    description = models.CharField("Mô tả", max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return self.name