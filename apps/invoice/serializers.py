# serializers.py
import decimal

from rest_framework import serializers
from apps.invoice.models import Invoice
from apps.user.serializers import UserSerializer
from apps.booking.serializers import BookingSerializer
from apps.invoice.utils import TotalAmountCalculator


class InvoiceListSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()
    booking = serializers.StringRelatedField()

    class Meta:
        model = Invoice
        fields = ('id', 'booking', 'customer', 'payment_method', 'total', 'payment_date')


class ProcessPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ('id', 'booking', 'payment_method', 'total')

    def validate(self, attrs):
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
        booking.status = 'PAID'
        booking.save()

    def set_room_available(self, booking):
        room = booking.room
        room.available = True
        room.save()


class InvoiceDetailSerializer(serializers.ModelSerializer):
    customer = UserSerializer()
    booking = BookingSerializer()

    class Meta:
        model = Invoice
        exclude = ('active', 'created_date', 'modified_date', 'deleted_date')
