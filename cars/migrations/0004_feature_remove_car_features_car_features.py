# Generated by Django 5.0.6 on 2024-06-10 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_description_alter_car_features'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='car',
            name='features',
        ),
        migrations.AddField(
            model_name='car',
            name='features',
            field=models.ManyToManyField(to='cars.feature'),
        ),
    ]
