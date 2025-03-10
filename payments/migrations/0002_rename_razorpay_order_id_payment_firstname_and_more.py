# Generated by Django 5.0.6 on 2024-06-27 16:33

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_alter_car_body_style'),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='razorpay_order_id',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='razorpay_payment_id',
            new_name='lastname',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='razorpay_signature',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='status',
        ),
        migrations.AddField(
            model_name='payment',
            name='car_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cars.car'),
        ),
        migrations.AddField(
            model_name='payment',
            name='city',
            field=models.CharField(default='city', max_length=100),
        ),
        migrations.AddField(
            model_name='payment',
            name='phone',
            field=models.IntegerField(default=9999999),
        ),
        migrations.AddField(
            model_name='payment',
            name='pincode',
            field=models.IntegerField(default=82756),
        ),
        migrations.AddField(
            model_name='payment',
            name='state',
            field=models.CharField(default='state', max_length=100),
        ),
        migrations.AddField(
            model_name='payment',
            name='street',
            field=models.CharField(default='city', max_length=100),
        ),
        migrations.AddField(
            model_name='payment',
            name='trial_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
