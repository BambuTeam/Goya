# Generated by Django 3.1.2 on 2020-12-02 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20201020_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='photo',
            field=models.ImageField(default='items/default.png', upload_to='items/'),
        ),
    ]
