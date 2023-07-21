# email_service.py
from django.core.mail import send_mail


def send_booking_email(booking, created):
    subject = f"Reserva {'creada' if created else 'actualizada'}: {booking.uuid}"
    message = f"Se ha {'creado' if created else 'actualizado'} la reserva con ID {booking.uuid}."
    send_mail(subject, message, 'your-email@example.com', [booking.guest.email])
