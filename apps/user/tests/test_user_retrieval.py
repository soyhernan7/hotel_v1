from django.urls import reverse
from rest_framework import status
from .base import BaseUserTest


class UserRetrievalTestCase(BaseUserTest):
    def setUp(self):
        super().setUp()
        self.url = reverse('users-detail', kwargs={'pk': self.user.pk})

    def test_user_can_be_retrieved(self):
        # Prueba que se puede recuperar un usuario que existe.
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
