from django.db import models

# Create your models here.


class House(models.Model):
    """Model definition for Houses"""
    name = models.CharField(max_length=140)
    prices_per_night = models.PositiveIntegerField(
        verbose_name='Price', help_text='Positive numbers only')
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        verbose_name='Pets allowed?',
        default=True, help_text='Does this house allow pets?')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
