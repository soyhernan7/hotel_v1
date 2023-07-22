from django.urls import reverse
from rest_framework import status
from .base import InvoiceSetupTestCase


class InvoiceRetrievalTestCase(InvoiceSetupTestCase):
    def test_invoice_can_be_retrieved(self):
        url = reverse('invoices-detail', kwargs={'pk': self.invoice.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
