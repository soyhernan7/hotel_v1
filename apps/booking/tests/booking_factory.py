# booking_factory.py
import factory
from datetime import datetime, timedelta
from apps.booking.models import Booking
from apps.room.tests.room_factory import RoomFactory
from apps.user.tests.user_factory import UserFactory


class BookingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Booking

    uuid = factory.Faker('uuid4')
    room = factory.SubFactory(RoomFactory)
    guest = factory.SubFactory(UserFactory)
    reservation_date = factory.Faker('date_time_this_year', before_now=True, after_now=False)
    checkin_date = datetime.now().date()
    checkout_date = factory.LazyAttribute(lambda obj: obj.checkin_date + timedelta(days=1))
    status = factory.Iterator(Booking.BookingStatus.choices)
