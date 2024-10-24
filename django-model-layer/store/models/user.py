from django.db import models


class User(models.Model):
    full_name = models.CharField("Họ Tên", max_length=20)
    display_name = models.CharField("Tên tài khoản", max_length=20)
    phone = models.CharField("SĐT", max_length=10, default="")
    # TODO validate phone field "only number":
        # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
        # phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list

    def __str__(self) -> str:
        return self.full_name