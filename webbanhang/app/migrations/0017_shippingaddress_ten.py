# Generated by Django 4.2.1 on 2023-06-06 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_orderitem_customer_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='ten',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
