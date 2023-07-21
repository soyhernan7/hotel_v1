from django.urls import reverse
from rest_framework import status
from .base import BaseUserTest

class UserRegistrationTestCase(BaseUserTest):
    def setUp(self):
        super().setUp()
        self.url = reverse('users-list')
        self.data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'name': 'Test',
            'last_name': 'User',
            'password': 'password123'
        }

    def test_user_can_be_registered(self):
        # Prueba que un usuario puede ser registrado.
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
