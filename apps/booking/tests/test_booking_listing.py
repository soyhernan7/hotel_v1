# booking/tests/test_booking_listing.py
from django.urls import reverse
from rest_framework import status
from apps.booking.tests.base import SetUpBookingAPITestCase


class BookingListingTestCase(SetUpBookingAPITestCase):
    def test_booking_can_be_listed(self):
        url = reverse('booking-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.booking_data['checkin_date'])
        self.assertContains(response, self.booking_data['checkout_date'])
