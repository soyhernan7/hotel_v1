# views.py
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, pagination
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from apps.invoice.models import Invoice

from apps.invoice.serializers import (
    ProcessPaymentSerializer,
    InvoiceDetailSerializer,
    InvoiceListSerializer
)


class InvoiceViewSet(viewsets.GenericViewSet):
    """
       Endpoints basada para la facturacion(Invoice).
    """
    model = Invoice
    serializer_class = InvoiceListSerializer
    detail_serializer_class = InvoiceDetailSerializer
    queryset = model.objects.filter(active=True)
    pagination_class = pagination.PageNumberPagination

    def get_object(self, pk):
        """ Obtiene una instancia del objeto con el id caso contraro muestra  error 404 si no hay.. """
        return get_object_or_404(self.model, pk=pk)

    def list(self, request):
        """
           Lista todas las facturas con paginación.
        """
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """
            Obtiene los detalles de una factura particular..
        """
        invoice = self.get_object(pk)
        detail_serializer = self.detail_serializer_class(invoice)
        return Response(detail_serializer.data)

    @action(detail=False, methods=['post'], url_path='process')
    def process_payment(self, request):
        """
            Procesa el pago de una factura.
        """
        process_serializer = ProcessPaymentSerializer(data=request.data)

        if process_serializer.is_valid():
            process_serializer.save()
            detail_serializer = self.detail_serializer_class(self.get_object(pk=process_serializer.data['id']))
            return Response(detail_serializer.data, status=status.HTTP_201_CREATED)

        return Response({'errors': process_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
