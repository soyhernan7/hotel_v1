from django.urls import reverse
from rest_framework import status
from .base import BaseUserTest


class UserUpdateTestCase(BaseUserTest):
    def setUp(self):
        super().setUp()
        self.url = reverse('users-detail', kwargs={'pk': self.user.pk})
        self.data = {
            'username': 'updateduser',
            'email': 'updated@example.com',
            'name': 'Updated',
            'last_name': 'User',
        }

    def test_user_can_be_updated(self):
        # Prueba que un usuario puede ser actualizado correctamente.
        response = self.client.put(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
