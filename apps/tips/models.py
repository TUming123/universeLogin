from django.contrib.auth.models import AbstractUser
from django.db import models


# GENDERCHOICE = {
#     ("male", "男"),
#     ("female", "女"),
# }


class TipMessage(models.Model):
    TID = models.CharField(max_length=50, verbose_name="TID")
    date = models.CharField(max_length=50, verbose_name="Date")
    amount = models.CharField(max_length=50, verbose_name="Amount")

    class Meta:
        verbose_name = "TipMessage"
        verbose_name_plural = verbose_name
        db_table = "TipMessage1"
        unique_together = (("TID", "date"),)

    def __str__(self):
        return "打赏(信息)用户" + self.TID


class TipUser(models.Model):
    ID = models.CharField(max_length=50, verbose_name="ID", primary_key=True)
    dpw = models.CharField(max_length=200, verbose_name="PSW")

    # gender = models.CharField(max_length=50, verbose_name="Gender", choices=GENDERCHOICE)

    class Meta:
        verbose_name = "TipUser"
        verbose_name_plural = verbose_name
        db_table = "TipUser1"

    def __str__(self):
        return "打赏用户" + self.ID
