from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    weight = models.FloatField()
    price = models.FloatField()
    created_at = models.CharField(max_length=50)
    updated_at = models.CharField(max_length=50)
