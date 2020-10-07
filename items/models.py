from django.db import models


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=500, null=True)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, null=False, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)
    date_creation = models.DateTimeField(auto_now_add=True)
    user_creation = models.CharField(max_length=45, null=True)
    date_update = models.DateTimeField(auto_now=True)
    user_update = models.CharField(max_length=45,null=True)
    photo = models.ImageField(upload_to='Items', default= 'default.img')

    def __str__(self):
        return self.name