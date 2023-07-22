# booking/tests/test_booking_creation.py
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from apps.booking.tests.base import SetUpBookingAPITestCase


class BookingCreationTestCase(SetUpBookingAPITestCase):
    def test_booking_can_be_created(self):
        url = reverse('booking-list')
        response = self.client.post(url, self.booking_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
