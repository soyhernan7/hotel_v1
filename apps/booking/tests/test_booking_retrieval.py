# booking/tests/test_booking_retrieval.py
from django.urls import reverse
from rest_framework import status
from apps.booking.tests.base import SetUpBookingAPITestCase


class BookingRetrievalTestCase(SetUpBookingAPITestCase):
    def test_booking_can_be_retrieved(self):
        url = reverse('booking-detail', kwargs={'pk': self.booking.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.booking_data['checkin_date'])
        self.assertContains(response, self.booking_data['checkout_date'])
