# Generated by Django 4.1.2 on 2022-10-27 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_order_customer_adress_order_total_amount_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order", old_name="total_amount", new_name="total_price",
        ),
    ]
