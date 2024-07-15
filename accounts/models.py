from django.db import models
from datetime import datetime



class Refunds(models.Model):
    user_refund_id = models.IntegerField(blank=True)
    car_refund_id = models.IntegerField()
    car_title = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

