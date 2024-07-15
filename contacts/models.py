from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    car_id = models.IntegerField()
    customer_need = models.CharField(max_length=100)
    car_title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(blank=True, default=datetime.now)


    def __str__(self):
        return self.email

class Favorites(models.Model):
    user_id = models.IntegerField(blank=True)
    car_id = models.IntegerField()
    car_title = models.CharField(max_length=100)
    created_date = models.DateTimeField(blank=True, default=datetime.now)


    def __str__(self):
        return self.car_title

class Payments(models.Model):
    car_id = models.IntegerField()
    car_title = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    pincode = models.IntegerField()
    phone = models.CharField(max_length=50)
    trial_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.trial_date}"
