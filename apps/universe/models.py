from django.db import models


class UniverseUser(models.Model):
    ID = models.CharField(max_length=50, verbose_name="ID", primary_key=True)
    dpw = models.CharField(max_length=200, verbose_name="PSW")
    # gender = models.CharField(max_length=50, verbose_name="Gender", choices=GENDERCHOICE)

    class Meta:
        verbose_name = "UniverseUser"
        verbose_name_plural = verbose_name
        db_table = "UniverseUser1"

class UnionUser(models.Model):
    FID = models.CharField(max_length=50, verbose_name="FID", unique=True)
    TID = models.CharField(max_length=50, verbose_name="TID", unique=True)
    UID = models.CharField(max_length=50, verbose_name="UID", unique=True)
    # gender = models.CharField(max_length=50, verbose_name="Gender", choices=GENDERCHOICE)

    class Meta:
        verbose_name = "UnionUser"
        verbose_name_plural = verbose_name
        db_table = "UnionUser1"