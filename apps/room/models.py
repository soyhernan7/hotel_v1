# room/models.py
from django.db import models


class Room(models.Model):
    class RoomTypes(models.TextChoices):
        SIMPLE = 'SIM', 'Simple'
        DOUBLE = 'DBL', 'Double'
        MATRIMONIAL = 'MAT', 'Matrimonial'
        SPECIAL = 'SPL', 'Special'

    type = models.CharField('Room Type',max_length=3,choices=RoomTypes.choices,default=RoomTypes.SIMPLE)
    description = models.TextField('Description')
    price_per_day = models.DecimalField('Price per Day', max_digits=7, decimal_places=2, null=True, blank=True)
    discount_rate = models.PositiveIntegerField('Discount Rate', default=0)
    is_available = models.BooleanField('Available',default=True)

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'
        ordering = ['type']

    def __str__(self):
        return f"{self.get_type_display()} - {self.description[:25]}..."

