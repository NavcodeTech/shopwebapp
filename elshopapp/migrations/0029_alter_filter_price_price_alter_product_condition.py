# Generated by Django 4.2 on 2023-04-17 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elshopapp', '0028_alter_filter_price_price_alter_product_condition_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter_price',
            name='price',
            field=models.CharField(choices=[('50000 TO 100000', '50000 TO 100000'), ('10000 TO 20000', '10000 TO 20000'), ('1000 TO 5000', '1000 TO 5000'), ('500', '500 TO 1000'), ('20000 TO 50000', '20000 TO 50000'), ('5000 TO 10000', '5000 TO 10000')], max_length=60),
        ),
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('New', 'New'), ('Old', 'Old')], max_length=100),
        ),
    ]