# Generated by Django 3.1.2 on 2020-10-12 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryLoads', '0004_inventoryload_provider'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventoryloaddetail',
            old_name='cantidad',
            new_name='quantity',
        ),
    ]
