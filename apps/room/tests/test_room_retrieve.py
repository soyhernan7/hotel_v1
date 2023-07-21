from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from apps.room.tests.room_factory import RoomFactory


class RoomRetrieveTestCase(APITestCase):
    def setUp(self):
        self.room = RoomFactory()

    def test_room_can_be_retrieved(self):
        # Prueba que se puede recuperar una cuarto existente.
        url = reverse('rooms-detail', kwargs={'pk': self.room.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
