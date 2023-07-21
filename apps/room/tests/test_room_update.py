from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from apps.room.models import Room
from apps.room.tests.room_factory import RoomFactory


class RoomUpdateTestCase(APITestCase):
    def setUp(self):
        self.room = RoomFactory()

    def test_room_can_be_updated(self):
        # Prueba que una cuarto puede ser actualizada correctamente.
        url = reverse('rooms-detail', kwargs={'pk': self.room.pk})
        data = {
            'type': Room.RoomTypes.SPECIAL,
            'description': 'Updated room',
            'price_per_day': '150.00',
            'discount_rate': '20',
            'is_available': 'False'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
