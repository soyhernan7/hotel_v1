# views.py
from rest_framework import viewsets, status, pagination
from rest_framework.decorators import action
from rest_framework.response import Response
from .email_service import send_booking_email
from .models import Booking
from .serializers import (
    BookingSerializer,
    BookingListSerializer
)


class BookingViewSet(viewsets.ModelViewSet):
    model = Booking
    serializer_class = BookingSerializer
    queryset = Booking.objects.filter(active=True)
    lookup_field = 'pk'
    pagination_class = pagination.PageNumberPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return BookingListSerializer
        if self.action == 'retrieve':
            return BookingListSerializer
        if self.action == 'partial_update':
            return BookingListSerializer
        return super().get_serializer_class()

    def list(self, request):
        """ Returns paginated list of bookings """
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_path='make')
    def book(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        reservation = serializer.save()
        # send_booking_email(reservation, created=True)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['patch'], url_path='cancel')
    def cancel(self, request, pk=None, **kwargs):
        reservation = self.get_object()
        data = {'status': 'CANCELLED'}
        serializer = self.get_serializer(reservation, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        reservation = serializer.save()
        send_booking_email(reservation, created=False)

        # return Response(serializer.data, status=status.HTTP_200_OK)