# Generated by Django 4.2.1 on 2023-06-06 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_shippingaddress_sodt'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='customer_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.shippingaddress'),
        ),
    ]
