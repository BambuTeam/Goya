from django.db import models
from items.models import Item

# Create your models here.


class Provider(models.Model):
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=300)
    email = models.EmailField()
    phone = models.CharField(max_length=45)
    contact_name = models.CharField(max_length=150)
    contac_email = models.EmailField()
    contact_phone = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class InventoryLoad(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=500)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    document_type = models.CharField(max_length=50)
    document_number = models.CharField(max_length=200)

    def __str__(self):
        return '{} number {} date {}'.formal(self.document_type,self.document_number,self.date)



class InventoryLoadDetail(models.Model):
    item = models.ForeignKey(Item, null=False, on_delete=models.PROTECT)
    cantidad = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


