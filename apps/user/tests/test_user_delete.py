from django.urls import reverse
from rest_framework import status
from .base import BaseUserTest


class UserDeleteTestCase(BaseUserTest):
    def setUp(self):
        super().setUp()
        self.url = reverse('users-detail', kwargs={'pk': self.user.pk})

    def test_user_can_be_deleted(self):
        # Prueba que un usuario puede ser borrado correctamente.
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

