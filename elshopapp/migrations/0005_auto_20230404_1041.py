# Generated by Django 3.2.4 on 2023-04-04 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elshopapp', '0004_auto_20230404_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter_price',
            name='price',
            field=models.CharField(choices=[('1000 TO 5000', '1000 TO 5000'), ('50000 TO 100000', '50000 TO 100000'), ('10000 TO 20000', '10000 TO 20000'), ('20000 TO 50000', '20000 TO 50000'), ('500', '500 TO 1000'), ('5000 TO 10000', '5000 TO 10000')], max_length=60),
        ),
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('Old', 'Old'), ('New', 'New')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Publish', 'Publish')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.CharField(choices=[('OUT OF STOCK', 'OUT OF STOCK'), ('IN STOCK', 'IN STOCK')], max_length=100),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elshopapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Product_images/img')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elshopapp.product')),
            ],
        ),
    ]
