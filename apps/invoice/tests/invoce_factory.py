# invoce_factory.py
import factory
from apps.invoice.models import Invoice
from apps.user.tests import user_factory
from apps.booking.tests import booking_factory


# class InvoiceFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Invoice
#
#     uuid = factory.Faker('uuid4')
#     booking = factory.SubFactory(booking_factory)
#     customer = factory.SubFactory(user_factory)
#     payment_method = factory.Iterator(Invoice.PaymentMethod.choices, getter=lambda c: c[0])
#     taxes = factory.Faker('pydecimal', left_digits=4, right_digits=2, positive=True)
#     room_fee = factory.Faker('pydecimal', left_digits=4, right_digits=2, positive=True)
#     total = factory.LazyAttribute(lambda number: number.room_fee + number.taxes)
#     description = factory.Faker('paragraph')
