# Generated by Django 5.0.6 on 2024-06-10 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_feature_remove_car_features_car_features'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='features',
        ),
        migrations.RemoveField(
            model_name='car',
            name='body_style',
        ),
        migrations.DeleteModel(
            name='Feature',
        ),
        migrations.AddField(
            model_name='car',
            name='features',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
