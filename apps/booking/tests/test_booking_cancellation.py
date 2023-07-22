# booking/tests/test_booking_cancellation.py
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from apps.booking.models import Booking
from apps.booking.tests.base import SetUpBookingAPITestCase


class BookingCancellationTestCase(SetUpBookingAPITestCase):
    def test_booking_can_be_cancelled(self):
        url = reverse('booking-cancel', kwargs={'pk': self.booking.pk})
        response = self.client.patch(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.status, Booking.BookingStatus.CANCELLED)
