# Generated by Django 3.2.4 on 2023-04-09 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elshopapp', '0011_auto_20230409_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter_price',
            name='price',
            field=models.CharField(choices=[('10000 TO 20000', '10000 TO 20000'), ('500', '500 TO 1000'), ('5000 TO 10000', '5000 TO 10000'), ('20000 TO 50000', '20000 TO 50000'), ('50000 TO 100000', '50000 TO 100000'), ('1000 TO 5000', '1000 TO 5000')], max_length=60),
        ),
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('Old', 'Old'), ('New', 'New')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.CharField(choices=[('OUT OF STOCK', 'OUT OF STOCK'), ('IN STOCK', 'IN STOCK')], max_length=100),
        ),
    ]