from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from apps.room.tests.room_factory import RoomFactory


class RoomDeleteTestCase(APITestCase):
    def setUp(self):
        self.room = RoomFactory()

    def test_room_can_be_deleted(self):
        #Prueba que un cuarto puede ser eliminado.
        url = reverse('rooms-detail', kwargs={'pk': self.room.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
