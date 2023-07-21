# serializers.py
import decimal

from rest_framework import serializers
from apps.invoice.models import Invoice
from apps.user.serializers import UserSerializer
from apps.booking.serializers import BookingSerializer
from apps.invoice.utils import TotalAmountCalculator


class InvoiceListSerializer(serializers.ModelSerializer):
    # Serializador para listar facturas.
    customer = serializers.StringRelatedField()
    booking = serializers.StringRelatedField()

    class Meta:
        model = Invoice
        fields = ('id', 'booking', 'customer', 'payment_method', 'total', 'payment_date')


class ProcessPaymentSerializer(serializers.ModelSerializer):
    # Serializador para procesar el pago de un invoicea.
    class Meta:
        model = Invoice
        fields = ('id', 'booking', 'payment_method', 'total')

    def validate(self, attrs):
        # Valida que la reserva esté en estado 'PENDING' y el total sea correcto antes de procesar el pago.
        booking = attrs['booking']
        total_amount = TotalAmountCalculator(booking).total_fees()

        if booking.status != 'PENDING':
            raise serializers.ValidationError(
                {'booking': f"La reserva ha sido  {booking.status}, no se puede procesar el pago."})

        if float(attrs['total']) != float(total_amount['total']):
            raise serializers.ValidationError(
                {'total': f"El monto total debe ser igual a '{total_amount['total']}', no se puede procesar el pago."})

        return attrs

    def create(self, validated_data):
        # Crea una factura y actualiza el estado de la reserva y la disponibilidad de la habitación.
        booking = validated_data['booking']
        total_amount = TotalAmountCalculator(booking).total_fees()

        self.update_booking_status(booking)
        self.set_room_available(booking)

        invoice = Invoice(**validated_data)
        invoice.customer = booking.guest
        invoice.room_fee = total_amount['room_charge']
        invoice.taxes = total_amount['taxes']
        invoice.total = total_amount['total']
        invoice.save()

        return invoice

    def update_booking_status(self, booking):
        # Actualiza el estado de la reserva a 'PAID'.\
        booking.status = 'PAID'
        booking.save()

    def set_room_available(self, booking):
        # Actualiza la disponibilidad de la habitación a True.
        room = booking.room
        room.available = True
        room.save()


class InvoiceDetailSerializer(serializers.ModelSerializer):
    # Serializador para ver detalles de una factura.
    customer = UserSerializer()
    booking = BookingSerializer()

    class Meta:
        model = Invoice
        exclude = ('active', 'created_date', 'modified_date', 'deleted_date')
