# Generated by Django 5.0 on 2024-01-03 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0019_remove_cart_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cook_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Pending', 'Packed'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], default='pending', max_length=50),
        ),
    ]
