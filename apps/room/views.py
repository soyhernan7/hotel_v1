# room/views.py
from rest_framework import viewsets,pagination
from apps.room.serializers import RoomSerializer


class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = RoomSerializer.Meta.model.objects.filter(is_available=True)
    pagination_class = pagination.PageNumberPagination
