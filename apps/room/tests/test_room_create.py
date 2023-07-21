from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from apps.room.models import Room


class RoomCreateTestCase(APITestCase):
    def test_room_can_be_created(self):
        # Prueba que un cuarto puede ser creado correctamente.
        url = reverse('rooms-list')
        data = {
            'type': Room.RoomTypes.SIMPLE,
            'description': 'Test room',
            'price_per_day': '100.00',
            'discount_rate': '10',
            'is_available': 'True'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
