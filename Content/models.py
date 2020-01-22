from django.db import models
from rest_framework import serializers

# Create your models here.

class Category(models.Model):
    kind = (('Laptop','laptop'),
            ('Mobile','mobile'),
            ('Home','home'))

    category = models.CharField(max_length=20, choices=kind , blank=True, default='home')

    def __str__(self):
        return self.category



class Item(models.Model):
    kinds = models.ForeignKey(Category, on_delete=models.CASCADE)
    name  = models.CharField(max_length=250, unique=True)
    def __str__(self):
        return self.name


class LaptopItem(models.Model):
    Laptopkind = (('NoteBook','notebook'),
                ('UltraBook','ultrabook'),
                ('NetBook','netbook'),
                ('ChromeBook','chromebook'))

    kind_status = models.CharField(max_length=20, choices=Laptopkind , default='notebook')
    brand       = models.CharField(max_length=250, null = True)
    price       = models.CharField(max_length=50, null=True)
    number      = models.IntegerField(null=True)
    made        = models.CharField(max_length=250, blank=True, null = True)
    dateadd     = models.DateField(null=True)
    name        = models.OneToOneField(Item, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.name, self.kind_status)
    class Meta:
        ordering = ["name"]

class Laptop(models.Model):
        name     = models.OneToOneField(LaptopItem, on_delete=models.CASCADE)
        pid      = models.IntegerField(help_text='10 character' ,default=0000000000, unique=True)
        model    = models.DateField(blank=True, null=True)
        color    = models.CharField(max_length=50, null=True)
        original = models.BooleanField(default="original" , null=True)
        ram      = models.CharField(max_length=200, null=True)
        graphic  = models.CharField(max_length=200, null=True)
        cpu      = models.CharField(max_length=200, null=True)

        cputype = (('DualCore','dualcore'),
                ('QualCore','qualcore'),
                ('CoreI3','corei3'),
                ('CoreI5','corei5'),
                ('CoreI7','corei7'),
                ('CoreI9','corei9'),
                ('Xeon','xeon'),
                ('Ryzen3','ryzen3'),
                ('Ryzen5','ryzen5'),
                ('Ryzen7','ryzen7'),
                ('Tegra K1','tegrak1'))
        cpu_status = models.CharField(max_length=20, choices=cputype , default='home')
        hdd        = models.CharField(max_length=200, null=True)

        os    = (('Windows','windows'),
                ('Linux','qualcore'),
                ('Mac','mac'),
                ('Google Chrome','googlechrome'),
                ('Windows7','windows7'),
                ('Windows8','windows8'),
                ('Windows9','windows9'),
                ('Windows19','windows10'))
        os_statuse = models.CharField(max_length=20, choices=os , default='windows')

        size = (('10','10'),
                ('12','12'),
                ('13','13'),
                ('14','14'),
                ('15','15'),
                ('17','17'),
                ('19','19'))
        size_status = models.CharField(max_length=20, choices=size)
        touchlcd   = models.BooleanField(default="No" , null=True)
        opaquelcd  = models.BooleanField(default="Yes" , null=True)
        image      = models.ImageField(upload_to='Content/static/images' , blank=True, null=True)
        details    = models.TextField(blank=True, null=True)



class MobileItem(models.Model):
    os = (('None','none'),
        ('Andriod','andriod'),
        ('IOS','ios'),
        ('Windsows Phone','windsowsphone'),
        ('Symbian ','symbian '),
        ('Black Berry','blackberry'),
        ('KaiOS ','kaios'))
    os_status = models.CharField(max_length=20, choices=os , blank=True, default='home')
    brand   = models.CharField(max_length=250, blank=True, null=True)
    made    = models.CharField(max_length=250, blank=True, null=True)
    price   = models.CharField(max_length=50, null=True)
    number  = models.IntegerField(null=True)
    model   = models.DateField(null=True)
    dateadd = models.DateField(blank=True, null=True)
    name    = models.OneToOneField(Item, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
    class Meta:
        ordering = ["name"]
    


class Mobile(models.Model):
     pid   = models.IntegerField(help_text='10 character',default=0000000000, unique=True)
     name  = models.OneToOneField(MobileItem, on_delete=models.CASCADE)
     color = models.CharField(max_length=50, null=True)
     lcd      = models.CharField(max_length=250, null = True)
     original = models.BooleanField(default="original" , null=True)
     camera   = models.CharField(max_length=250, null = True)
     ram      =  models.CharField(max_length=250, null = True)
     cpu      = models.CharField(max_length=250, null = True)
     memory   = models.CharField(max_length=250, null = True)
     sizelcd  = models.CharField(max_length=250, null = True)
     touchlcd = models.BooleanField(default="Yes" , null=True)
     image    = models.ImageField(upload_to='Content/static/images' , blank=True, null=True)
     details  = models.TextField(blank=True, null=True)



class HomeItem(models.Model):
    name  = models.OneToOneField(Item, on_delete=models.CASCADE)
    pid   = models.IntegerField(help_text='10 character',default=0000000000, unique=True)

    kind = (('Digital','dogotal'),
            ('Kitchen','kitchen'),
            ('Other','other'))
    kind_status = models.CharField(max_length=20, choices=kind , blank=True, default='home')
    brand = models.CharField(max_length=250, blank=True, null = True)
    made  = models.CharField(max_length=250, blank=True, null = True)
    price = models.CharField(max_length=50, null=True)
    number = models.IntegerField(null=True)
    model = models.DateField(blank=True, null=True)
    date  = models.DateField(blank=True, null=True)
    color = models.CharField(max_length=50, null=True)
    original = models.BooleanField(default="original" , blank=True, null=True)
    image    = models.ImageField(upload_to='Content/static/images' , blank=True, null=True)
    details  = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["name"]




