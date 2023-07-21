# models.py
from django.db import models
from shortuuidfield import ShortUUIDField

from apps.base.models import BaseModel
from apps.booking.models import Booking
from apps.user.models import User


class Invoice(BaseModel):
    class PaymentMethod(models.TextChoices):
        CREDIT_CARD = 'CREDIT_CARD', 'Tarjeta Credito'
        CASH = 'CASH', 'Efectivo'
        QR = 'QR', 'QR'

    uuid = ShortUUIDField()
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50, choices=PaymentMethod.choices)
    taxes = models.DecimalField(max_digits=10, decimal_places=2)
    room_fee = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-payment_date']
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'
