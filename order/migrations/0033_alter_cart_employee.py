# Generated by Django 3.2.6 on 2024-01-11 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0032_auto_20240108_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='employee',
            field=models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='order.employee'),
        ),
    ]
