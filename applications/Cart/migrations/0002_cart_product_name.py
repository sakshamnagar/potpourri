# Generated by Django 2.1 on 2021-05-26 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Product', '0001_initial'),
        ('Cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='Product_Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.Product'),
        ),
    ]
