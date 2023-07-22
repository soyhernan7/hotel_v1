# serializers.py
from rest_framework import serializers
from apps.booking.models import Booking
from apps.room.serializers import RoomSerializer
from apps.user.serializers import UserRegisterSerializer
from datetime import date
from apps.invoice.utils import TotalAmountCalculator

CHECKIN_DATE_ERROR = "'checkin_date' debe ser mayor o igual a 'today'"
CHECKOUT_DATE_ERROR = "'checkout_date' debe ser mayor o igual a 'checkin_date'"
ROOM_NOT_AVAILABLE_ERROR = "La habitación no está disponible."


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        # fields = 'uuid,reservation_date,checkin_date,checkout_date,total_nights'

    def validate(self, data):
        # Valida los datos del modelo Booking antes de guardarlos.
        self._validate_checkin_date(data)
        self._validate_checkout_date(data)
        self._validate_room_availability(data)

        return data

    def _validate_checkin_date(self, data):
        # Valida que 'checkin_date' sea mayor o igual a la fecha actual.
        checkin_date = data.get('checkin_date')
        if checkin_date and checkin_date < date.today():
            raise serializers.ValidationError(
                {'checkin_date': "'checkin_date' debe ser mayor o igual a 'today'"}
            )

    def _validate_checkout_date(self, data):
        # Valida que 'checkout_date' sea mayor o igual a 'checkin_date'.
        checkin_date = data.get('checkin_date')
        checkout_date = data.get('checkout_date')
        if checkin_date and checkout_date and checkin_date > checkout_date:
            raise serializers.ValidationError(
                {'checkout_date': "'checkout_date' debe ser mayor o igual a 'checkin_date'"}
            )

    def _validate_room_availability(self, data):
        # Valida que la habitación esté disponible.
        room = data.get('room')
        if room and not room.is_available:
            raise serializers.ValidationError(
                {'room': "La habitación no está disponible."}
            )

    def create(self, validated_data):
        # Crea una reserva y marca la habitación como no disponible.
        room = validated_data['room']
        room.available = False
        room.save()

        reservation = Booking(**validated_data)
        reservation.save()

        return reservation

    def to_representation(self, instance):
        # Convierte una instancia de booking en una representación customizada..
        fees = TotalAmountCalculator(instance).total_fees()
        return {
            'id': instance.id,
            'uuid': instance.uuid,
            'reservation_date': instance.reservation_date,
            'checkin_date': instance.checkin_date,
            'checkout_date': instance.checkout_date,
            'guest': instance.guest.__str__(),
            'room': instance.room.__str__(),
            'price_per_night': instance.room.price_per_day,
            'total_nights': instance.get_total_nights(),
            'room_charge': fees['room_charge'],
            'taxes': fees['taxes'],
            'total': fees['total'],
            'status': instance.status,
        }


class BookingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def to_representation(self, instance):
        # Convierte una instancia de booking en una representación customizada..
        return {
            'id': instance.id,
            'uuid': instance.uuid,
            'reservation_date': instance.reservation_date,
            'checkin_date': instance.checkin_date,
            'checkout_date': instance.checkout_date,
            'total_nights': instance.get_total_nights(),
            'guest': instance.guest.__str__(),
            'room': instance.room.__str__(),
            'status': instance.status,
        }


class BookingViewSerializer(serializers.ModelSerializer):
    guest = UserRegisterSerializer()
    room = RoomSerializer()

    class Meta:
        model = Booking
        fields = '__all__'

    def to_representation(self, instance):
        # Convierte una instancia de reserva en una representación personalizada para la vista detallada.
        fees = TotalAmountCalculator(instance).total_fees()
        return {
            'id': instance.id,
            'uuid': instance.uuid,
            'reservation_date': instance.reservation_date,
            'checkin_date': instance.checkin_date,
            'checkout_date': instance.checkout_date,
            'guest': instance.guest.__str__(),
            'room': instance.room.__str__(),
            'price_per_night': instance.room.price_per_day,
            'total_nights': instance.get_total_nights(),
            'room_charge': fees['room_charge'],
            'taxes': fees['taxes'],
            'total': fees['total'],
            'status': instance.status,
        }


class BookingStatusSerializer(BookingViewSerializer):
    class Meta:
        model = Booking
        # fields = ('id', 'status')
        fields = '__all__'

    def validate(self, data):
        # Valida que la reserva solo se pueda cambiar si en estado 'PENDING'.
        if self.instance.status != 'PENDING':
            raise serializers.ValidationError(
                {
                    'status': f"""The reservation status is already in {self.instance.status} status, cannot be CANCELLED"""}
            )
        return data
