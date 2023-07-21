# tests.py
from decimal import Decimal
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

# from apps.invoice.models import Invoice
# from apps.invoice.tests.invoce_factory import InvoiceFactory
# from apps.invoice.utils import TotalAmountCalculator
# from apps.booking.models import Booking
# from apps.user.tests.user_factory import UserFactory
# from apps.room.models import Room
# from apps.room.tests.room_factory import RoomFactory
# from apps.booking.tests.booking_factory import BookingFactory


# class InvoiceViewTestCase(TestCase):
#
#     def setUp(self):
#         self.client = APIClient()
#         self.user = UserFactory()
#         self.room = RoomFactory()
#         self.booking = BookingFactory(room=self.room, guest=self.user)
#         self.invoice = InvoiceFactory(booking=self.booking, customer=self.user)
#
#     def test_retrieve_invoice(self):
#         response = self.client.get(f'/api/invoices/{self.invoice.uuid}/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['uuid'], str(self.invoice.uuid))
#
#     def test_invoice_payment(self):
#         data = {
#             'booking': self.booking.uuid,
#             'payment_method': 'CREDIT_CARD',
#             'total': self.invoice.total
#         }
#         response = self.client.post('/api/invoices/process/', data=data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.booking.refresh_from_db()
#         self.assertEqual(self.booking.status, 'PAID')
#         self.invoice.refresh_from_db()
#         self.assertEqual(self.invoice.payment_method, 'CREDIT_CARD')
