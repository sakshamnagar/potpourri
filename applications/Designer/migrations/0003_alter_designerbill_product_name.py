# Generated by Django 5.0 on 2023-12-21 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Designer', '0002_designerbill_product_name'),
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designerbill',
            name='product_name',
            field=models.ManyToManyField(blank=True, to='Product.product'),
        ),
    ]
