from django.urls import reverse
from rest_framework import status
from .base import InvoiceSetupTestCase


class InvoiceCreationTestCase(InvoiceSetupTestCase):
    def test_invoice_can_be_created(self):
        url = reverse('invoices-process-payment')
        response = self.client.post(url, self.invoice_data)
        if response.status_code != status.HTTP_201_CREATED:
            print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
