from django.db import models

# Create your models here.
class DeliveryType(models.Model):
    name = models.CharField(max_length=200)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Delivery(models.Model):
    delibery_type = models.ForeignKey(DeliberyType, null=False, on_delete = models.PROTECT)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    delibery_date = models.DateField()
    phone = models.IntegerField()
    zip_nubmer = models.SmallIntegerField()
    address1 = models.TextField(max_length=800)
    city = models.CharField(max_length=50)
    notes = models.TextField(500)
    company_name = models.CharField(max_length=150)

    def __str__(self):
        return '{} {}'.format(self.first_name,self.last_name)
    


class Order(models.Model):
    order_type = models.CharField(max_length=145)
    rush_order = models.BooleanField(default=True)
    order_description = models.TextField()
    order_date = models.DateField(auto_now_add=True)
    delibery_date = models.DateField()
    state = models.CharField(max_length=11)


class Basket(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name
    


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.PROTECT)
    basquet = models.ForeignKey(Basket, null =False, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()







