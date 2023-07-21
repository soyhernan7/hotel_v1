# booking/tests/test_booking.py
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from apps.booking.models import Booking
from apps.user.tests.user_factory import UserFactory
from apps.room.tests.room_factory import RoomFactory
from datetime import date, timedelta


class BookingAPITestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        # Configuracion  par todas las pruebas de la clase BookingAPITestCase.
        super().setUpClass()
        cls.room = RoomFactory()
        cls.guest = UserFactory()
        cls.booking_data = {
            'room': cls.room.id,
            'guest': cls.guest.id,
            'checkin_date': date.today().isoformat(),
            'checkout_date': (date.today() + timedelta(days=5)).isoformat(),
        }
        cls.booking = Booking.objects.create(
            room=cls.room,
            guest=cls.guest,
            checkin_date=cls.booking_data['checkin_date'],
            checkout_date=cls.booking_data['checkout_date'],
        )

    def test_booking_can_be_created(self):
        # Prueba qe una reserva puede ser creada correctamente.
        url = reverse('booking-list')
        response = self.client.post(url, self.booking_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_booking_can_be_retrieved(self):
        # Prueba oara recuperar una reserva existente.
        url = reverse('booking-detail', kwargs={'pk': self.booking.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.booking_data['checkin_date'])
        self.assertContains(response, self.booking_data['checkout_date'])

    def test_booking_can_be_cancelled(self):
        # Prueba que una reserva puede ser CANCELLED.
        url = reverse('booking-cancel', kwargs={'pk': self.booking.pk})
        response = self.client.patch(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.status, Booking.BookingStatus.CANCELLED)

    def test_booking_cancellation_with_invalid_dates(self):
        # Prueba que la cancelacion de una reserva con fechas erroneas sale código estado 400.
        url = reverse('booking-cancel', kwargs={'pk': self.booking.pk})
        past_date = (date.today() - timedelta(days=5)).isoformat()
        data = {'checkin_date': past_date, 'checkout_date': past_date}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_booking_can_be_listed(self):
        # Prueba para listar todas las reservas existentes.
        url = reverse('booking-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.booking_data['checkin_date'])
        self.assertContains(response, self.booking_data['checkout_date'])
