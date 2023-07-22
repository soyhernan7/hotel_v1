# invoice/tests/test_listing.py
from django.urls import reverse
from rest_framework import status
from .base import InvoiceSetupTestCase


class InvoiceListingTestCase(InvoiceSetupTestCase):
    def test_invoice_can_be_listed(self):
        url = reverse('invoices-list')
        response = self.client.get(url)
        response_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response_data['results']), 1)
