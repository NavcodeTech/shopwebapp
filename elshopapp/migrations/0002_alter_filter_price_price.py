# Generated by Django 3.2.4 on 2023-04-04 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elshopapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter_price',
            name='price',
            field=models.CharField(choices=[('1000 TO 5000', '1000 TO 5000'), ('50000 TO 100000', '50000 TO 100000'), ('500', '500 TO 1000'), ('5000 TO 10000', '5000 TO 10000'), ('20000 TO 50000', '20000 TO 50000'), ('10000 TO 20000', '10000 TO 20000')], max_length=60),
        ),
    ]
