# room/serializers.py.py
from rest_framework import serializers
from apps.room.models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'type', 'description', 'price_per_day', 'discount_rate', 'is_available']
