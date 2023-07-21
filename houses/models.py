from django.db import models

# Create your models here.


class House(models.Model):
    """Model definition for Houses"""
    name = models.CharField(max_length=140)
    prices_per_night = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(default=True)
