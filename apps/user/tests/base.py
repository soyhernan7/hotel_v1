from rest_framework.test import APITestCase
from apps.user.tests.user_factory import UserFactory


class BaseUserTest(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('testpassword')
        self.user.save()
