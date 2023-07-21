from django.urls import reverse
from rest_framework import status
from .base import BaseUserTest

class UserListTestCase(BaseUserTest):
    def setUp(self):
        super().setUp()
        self.url = reverse('users-list')

    def test_user_list(self):
        # Prueba que se pueden listar a los usuarios que existe.
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
