# Generated by Django 3.1.2 on 2020-10-05 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(max_length=500, null=True)),
                ('stock', models.PositiveIntegerField()),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('user_creation', models.CharField(max_length=45, null=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('user_update', models.CharField(max_length=45, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='items.category')),
                ('tags', models.ManyToManyField(to='items.Tag')),
            ],
        ),
    ]
