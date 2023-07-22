# invoice/tests/setup.py
from rest_framework.test import APITestCase
from apps.invoice.tests.invoce_factory import InvoiceFactory
from apps.booking.tests.booking_factory import BookingFactory
from apps.user.tests.user_factory import UserFactory
from apps.invoice.utils import TotalAmountCalculator


class InvoiceSetupTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.booking = BookingFactory(status="PENDING")
        total_calculator = TotalAmountCalculator(cls.booking)
        total_fees = total_calculator.total_fees()
        cls.customer = UserFactory()
        cls.invoice = InvoiceFactory(booking=cls.booking, customer=cls.customer)
        cls.invoice_data = {
            'booking': cls.invoice.booking.id,
            'customer': cls.invoice.customer.id,
            'payment_method': "CREDIT_CARD",
            'total': total_fees['total'],
            'payment_date': cls.invoice.payment_date.isoformat(),
        }
