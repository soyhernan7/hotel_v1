from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from apps.room.tests.room_factory import RoomFactory


class RoomListTestCase(APITestCase):
    def setUp(self):
        self.room = RoomFactory()

    def test_room_can_be_listed(self):
        # Prueba que se pueden listar todas las habitaciones.
        url = reverse('rooms-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
