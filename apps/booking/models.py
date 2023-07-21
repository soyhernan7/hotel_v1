#models.py
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from apps.user.models import User
from apps.base.models import BaseModel
from apps.room.models import Room
import uuid


class Booking(BaseModel):
    class BookingStatus(models.TextChoices):
        PENDING = 'PENDING', _('Pending')
        PAID = 'PAID', _('Paid')
        CANCELLED = 'CANCELLED', _('Cancelled')

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Room ID')
    guest = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Guest ID')
    reservation_date = models.DateTimeField('Reservation Date', auto_now_add=True)
    checkin_date = models.DateField('Check-In Date')
    checkout_date = models.DateField('Check-Out Date')
    status = models.CharField('Reservation State', max_length=20, choices=BookingStatus.choices,
                              default=BookingStatus.PENDING)

    class Meta:
        ordering = ['-reservation_date']
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return f'Reservation {self.uuid} by {self.guest.username}'

    def clean(self):
        super().clean()
        if self.checkout_date <= self.checkin_date:
            raise ValidationError({
                'checkout_date': _('Check-Out date should be later than Check-In date.')
            })

    def get_total_nights(self):
        diff = self.diff_days()
        return 1 if diff <= 0 else diff

    def diff_days(self):
        return (self.checkout_date - self.checkin_date).days

