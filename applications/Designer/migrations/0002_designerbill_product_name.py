# Generated by Django 2.1 on 2021-05-26 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Designer', '0001_initial'),
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='designerbill',
            name='product_name',
            field=models.ManyToManyField(to='Product.Product'),
        ),
    ]