from django.db import models
from items.models import Item
from django.contrib.auth.models import User

# Create your models here.


class Provider(models.Model):
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=300, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=45, null= True)
    site = models.URLField(null=True)
    contact_name = models.CharField(max_length=150, null=True)
    contac_email = models.EmailField(null=True)
    contact_phone = models.PositiveIntegerField(null=True)
    last_user_update = models.CharField(max_length=45,null=True)
    last_date_update = models.DateField(auto_now = True, null=True)
    def __str__(self):
        return self.name


class InventoryLoad(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    description = models.TextField(max_length=500)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    document_type = models.CharField(max_length=50, null=False, blank=False, default='N/A')
    document_number = models.CharField(max_length=200, null=False, blank=False, default='N/A')
    provider = models.ForeignKey(Provider, null = False, on_delete=models.PROTECT)
    last_user_update = models.ForeignKey(User, on_delete = models.PROTECT)
    last_date_update = models.DateField(auto_now = True)


    def __str__(self):
        return '{} number {} date {}'.format(self.document_type,self.document_number,self.date)



class InventoryLoadDetail(models.Model):
    item = models.ForeignKey(Item, null=False, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventoryLoad = models.ForeignKey(InventoryLoad, null = False, on_delete= models.PROTECT)
    last_user_update = models.ForeignKey(User, on_delete = models.PROTECT)
    last_date_update = models.DateField(auto_now = True)

    def __str__(self):
        return '{} {} {}'.format(self.inventoryLoad.document_type, self.inventoryLoad.document_number, self.item.name)



