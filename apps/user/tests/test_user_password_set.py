from django.urls import reverse
from rest_framework import status
from .base import BaseUserTest


class UserPasswordSetTestCase(BaseUserTest):
    def setUp(self):
        super().setUp()
        self.client.login(username=self.user.username, password='testpassword')
        self.url = reverse('users-set-password', kwargs={'pk': self.user.pk})
        self.data = {
            'password': 'newpassword',
            'password2': 'newpassword'
        }

    # def test_user_password_can_be_set(self):
    #     response = self.client.patch(self.url, self.data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
