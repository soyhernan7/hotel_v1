# booking/tests/setup.py
from rest_framework.test import APITestCase
from apps.booking.tests.booking_factory import BookingFactory
from apps.user.tests.user_factory import UserFactory
from apps.room.tests.room_factory import RoomFactory


class SetUpBookingAPITestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.room = RoomFactory()
        cls.guest = UserFactory()
        cls.booking = BookingFactory(room=cls.room, guest=cls.guest)
        cls.booking_data = {
            'room': cls.booking.room.id,
            'guest': cls.booking.guest.id,
            'checkin_date': cls.booking.checkin_date.isoformat(),
            'checkout_date': cls.booking.checkout_date.isoformat(),
        }
