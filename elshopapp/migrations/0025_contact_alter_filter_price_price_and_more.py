# Generated by Django 4.2 on 2023-04-17 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elshopapp', '0024_alter_filter_price_price_alter_product_condition_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=200)),
                ('message', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='filter_price',
            name='price',
            field=models.CharField(choices=[('50000 TO 100000', '50000 TO 100000'), ('10000 TO 20000', '10000 TO 20000'), ('500', '500 TO 1000'), ('1000 TO 5000', '1000 TO 5000'), ('5000 TO 10000', '5000 TO 10000'), ('20000 TO 50000', '20000 TO 50000')], max_length=60),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Publish', 'Publish')], max_length=100),
        ),
    ]
