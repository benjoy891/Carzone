# Generated by Django 5.0.6 on 2024-06-27 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_rename_razorpay_order_id_payment_firstname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='car_id',
            new_name='car',
        ),
    ]
