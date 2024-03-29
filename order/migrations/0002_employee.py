# Generated by Django 5.0 on 2023-12-30 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_id', models.CharField(blank=True, max_length=100, null=True)),
                ('employee_name', models.CharField(max_length=100)),
                ('employee_address', models.CharField(max_length=100)),
                ('employee_mobile', models.IntegerField(default=True)),
                ('pin', models.IntegerField()),
                ('department', models.CharField(default=True, max_length=50)),
                ('added_by', models.CharField(default=True, max_length=50)),
                ('added_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.IntegerField(default=1)),
            ],
        ),
    ]
