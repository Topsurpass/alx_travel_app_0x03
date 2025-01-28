# listings/tasks.py

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Booking

@shared_task
def send_booking_confirmation_email(recipient_email, booking_id):
    try:
        booking = Booking.objects.select_related('listing', 'user').get(id=booking_id)
        
        total_nights = (booking.end_date - booking.start_date).days
        total_price = total_nights * booking.listing.price_per_night
        
        subject = f'Booking Confirmation #{booking_id}'
        message = f"""
        Thank you for your booking, {booking.user.username}!

        Booking Details:
        --------------------------
        Property: {booking.listing.title}
        Location: {booking.listing.location}
        Price per night: ${booking.listing.price_per_night:.2f}
        Check-in Date: {booking.start_date}
        Check-out Date: {booking.end_date}
        Total Nights: {total_nights}
        Total Price: ${total_price:.2f}
        
        We hope you enjoy your stay!
        """
        
        html_message = f"""
        <h3>Thank you for your booking, {booking.user.username}!</h3>
        
        <h4>Booking Details:</h4>
        <ul>
            <li><strong>Property:</strong> {booking.listing.title}</li>
            <li><strong>Location:</strong> {booking.listing.location}</li>
            <li><strong>Price per night:</strong> ${booking.listing.price_per_night:.2f}</li>
            <li><strong>Check-in Date:</strong> {booking.start_date}</li>
            <li><strong>Check-out Date:</strong> {booking.end_date}</li>
            <li><strong>Total Nights:</strong> {total_nights}</li>
            <li><strong>Total Price:</strong> ${total_price:.2f}</li>
        </ul>
        
        <p>We hope you enjoy your stay!</p>
        """

        send_mail(
            subject,
            message.strip(),
            settings.DEFAULT_FROM_EMAIL,
            [recipient_email],
            html_message=html_message,
            fail_silently=False
        )
        
    except Booking.DoesNotExist:
        print(f"Booking with id {booking_id} does not exist")
    except Exception as e:
        print(f"Failed to send confirmation email: {str(e)}")