# Generated by Django 4.2 on 2023-04-17 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elshopapp', '0027_alter_filter_price_price_alter_product_stock_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter_price',
            name='price',
            field=models.CharField(choices=[('500', '500 TO 1000'), ('1000 TO 5000', '1000 TO 5000'), ('10000 TO 20000', '10000 TO 20000'), ('20000 TO 50000', '20000 TO 50000'), ('5000 TO 10000', '5000 TO 10000'), ('50000 TO 100000', '50000 TO 100000')], max_length=60),
        ),
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('Old', 'Old'), ('New', 'New')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('Publish', 'Publish'), ('Draft', 'Draft')], max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(blank=True, default='2001-08-02'),
        ),
    ]
