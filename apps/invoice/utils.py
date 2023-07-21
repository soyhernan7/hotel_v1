#util.py
from decimal import Decimal, ROUND_HALF_UP
from apps.booking.models import Booking


class TotalAmountCalculator:
    TAX_RATE = Decimal('0.13')

    def __init__(self, reservation: Booking):
        self.reservation = reservation

    def calculate_room_charge(self):
        return self._room_price_per_day() * self._total_nights()

    def calculate_taxes(self):
        return self.calculate_room_charge() * self.TAX_RATE

    def calculate_total(self):
        return self.calculate_room_charge() + self.calculate_taxes()

    def total_fees(self):
        room_charge = self.calculate_room_charge()
        taxes = self.calculate_taxes()
        total = self.calculate_total()

        return {
            "room_charge": room_charge.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP),
            "taxes": taxes.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP),
            "total": total.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP),
        }

    def _room_price_per_day(self):
        return Decimal(self.reservation.room.price_per_day)

    def _total_nights(self):
        return Decimal(self.reservation.get_total_nights())
