# Generated by Django 3.2.6 on 2023-12-31 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_rename_category_name_dish_dish_category_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='dish_category_id',
        ),
        migrations.AddField(
            model_name='dish',
            name='dish_category',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, to='order.dish_category'),
        ),
    ]
