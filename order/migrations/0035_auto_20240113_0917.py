# Generated by Django 3.2.6 on 2024-01-13 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0034_alter_cart_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetail',
            name='dish_name',
        ),
        migrations.AddField(
            model_name='dish',
            name='dish_marathi_name',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='dish_marathi_name',
            field=models.CharField(default=True, max_length=100),
        ),
    ]
