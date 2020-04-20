from django.db import models


class Message(models.Model):
    MID = models.CharField(max_length=50, verbose_name="MID")
    name = models.CharField(max_length=50, verbose_name="Name")
#                                            comments
    email = models.EmailField(verbose_name="Mail", primary_key=True)
#                             defualt max length = 254
    address = models.CharField(max_length=100, verbose_name="Address")
    message = models.TextField(verbose_name="Address")
    date = models.CharField(max_length=50, verbose_name="Date")

    # def __init__(self):
    #     self.name = ""
    #     self.message = ""
    #     self.email = ""
    #     self.address = ""

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = verbose_name
        db_table = "Message1"
        unique_together = (("MID", "date"),)


class MessageUser(models.Model):
    ID = models.CharField(max_length=50, verbose_name="ID", primary_key=True)
    dpw = models.CharField(max_length=200, verbose_name="PSW")
    # def __init__(self):
    #     self.name = ""
    #     self.message = ""
    #     self.email = ""
    #     self.address = ""

    class Meta:
        verbose_name = "MessageUser1"
        verbose_name_plural = verbose_name
        db_table = "MessageUser1"

    def __str__(self):
        return self.ID
