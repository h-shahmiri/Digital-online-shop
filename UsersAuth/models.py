from django.db import models
from django.contrib.auth.models import User
from Content.models import Item , Category

# Create your models here.
class UserAddress(models.Model):
    state = (('Tehran','tehran'),
            ('Soon','soon'))
    state_choice = models.CharField(max_length=250, choices=state, null=True)

    city = (('Tehran','tehran'),
            ('Baharestan','baharestan'),
            ('Shemiranat','shemiranat'),
            ('Robat Karim','robat karim'),
            ('Firozkouh','firozkouh'),
            ('Varamin','varamin'),
            ('Eslamshahr','eslamshahr'),
            ('Rey','rey'),
            ('Pishya','pishya'),
            ('Ghods','ghods'),
            ('Malard','Malard'),
            ('Shahriar','shahriar'),
            ('Damavand','damavand'))
    city_choice = models.CharField(max_length=250, choices=state, null=True)
    address  = models.CharField(max_length=250, null=True, blank=True)
    post_code = models.IntegerField(unique=True, default=None, null=True)

    def __str__(self):
        return str(self.address)



class Orders(models.Model):
    cart        = models.CharField(max_length=250, null=True, blank=True)
    item_list   = models.ForeignKey(Item , on_delete=models.CASCADE)
    send_price  = models.IntegerField(null=True)
    factor_id   = models.IntegerField()
    factor_item = models.CharField(max_length=250, null=True)
    factor_date = models.DateField(null=True)
    factor_pay  = models.BooleanField(null=True)
    Delivery    = models.BooleanField(null=True)
    factor_price = models.IntegerField()
    Delivery_time = models.DateTimeField()
    

class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    address     = models.ForeignKey(UserAddress,  on_delete=models.CASCADE)
    national_code = models.IntegerField(unique=True, null=True, blank=True)
    phone_numb  = models.TextField(null=True, default=None)
    email       = models.EmailField(null=True, unique=True, default=None)
    score       = models.IntegerField(null=True,  blank=True)

    def __str__(self):
        return str(self.user)