from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField(max_length=500, null= True)
    last_user_update = models.ForeignKey(User, on_delete = models.PROTECT)
    last_date_update = models.DateField(auto_now = True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=500, null=True)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, null=False, on_delete=models.PROTECT)
    last_user_update = models.ForeignKey(User, on_delete = models.PROTECT)
    last_date_update = models.DateField(auto_now = True)
    photo = models.ImageField(upload_to='items/', default= 'items/default.png')


    def __str__(self):
        return self.name


    
