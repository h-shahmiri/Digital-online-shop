from django.db import models
from Content.models import *
# Create your models here.

class Factors(models.Model):

    cart        = models.ForeignKey(Item , on_delete=models.CASCADE)
    price       = models.IntegerField(null=True)
    send_price  = models.IntegerField(null=True)
    factor_id   = models.IntegerField()
    factor_address = models.CharField(max_length=250, null=True)
    factor_date = models.DateTimeField(null=True)
    prepayment  = models.IntegerField()
    factor_pay  = models.BooleanField(null=True)
    Delivery_time = models.DateTimeField(null=True, blank=True)
    