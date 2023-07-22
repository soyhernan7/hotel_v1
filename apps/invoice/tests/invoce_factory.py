# invoice_factory.py
import factory
from apps.invoice.models import Invoice
from apps.booking.tests.booking_factory import BookingFactory
from apps.user.tests.user_factory import UserFactory


class InvoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Invoice

    uuid = factory.Faker('uuid4')
    booking = factory.SubFactory(BookingFactory)
    customer = factory.SubFactory(UserFactory)
    payment_method = factory.Iterator(Invoice.PaymentMethod.choices)
    taxes = factory.Faker('pydecimal', left_digits=5, right_digits=2, positive=True)
    room_fee = factory.Faker('pydecimal', left_digits=5, right_digits=2, positive=True)
    total = factory.LazyAttribute(lambda obj: obj.room_fee + obj.taxes)
    payment_date = factory.Faker('date_this_month', before_today=True, after_today=False)
    description = factory.Faker('text')
