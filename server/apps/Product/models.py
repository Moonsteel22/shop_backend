from django.db import models

class Product(models.Model):
    producer = models.CharField(max_length=25)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    weight = models.CharField(max_length=7)
    received_date = models.DateTimeField(auto_now=True)
    img_url = models.CharField(max_length=40, blank=True)
    price = models.IntegerField(blank=True, default=0)
    amount = models.PositiveIntegerField(default=0)

