# factories.py
import factory
from datetime import datetime, timedelta
from apps.booking.models import Booking
from apps.user.tests import user_factory
from apps.room.tests import room_factory


# class BookingFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Booking
#
#     uuid = factory.Faker('uuid4')
#     room = factory.SubFactory(room_factory)
#     guest = factory.SubFactory(user_factory)
#     reservation_date = factory.Faker('date_time_this_year', before_now=True, after_now=False)
#     checkin_date = factory.LazyAttribute(lambda obj: datetime.now().date())
#     checkout_date = factory.LazyAttribute(lambda obj: obj.checkin_date + timedelta(days=1))
#     status = factory.Iterator(Booking.BookingStatus.choices, getter=lambda c: c[0])
