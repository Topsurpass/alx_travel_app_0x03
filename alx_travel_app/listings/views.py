from rest_framework import viewsets
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer
from .tasks import send_booking_confirmation_email


class ListingViewSet(viewsets.ModelViewSet):
	"""
	A viewset for viewing and editing listing instances.

	This viewset provides `list`, `create`, `retrieve`, `update`, and `destroy` actions for the Listing model.
	"""
	queryset = Listing.objects.all()
	serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
	"""
	A viewset for viewing and editing booking instances.

	This viewset provides `list`, `create`, `retrieve`, `update`, and `destroy` actions for the Booking model.
	"""
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer

	def perform_create(self, serializer):
		booking = serializer.save()
		# Trigger the email task asynchronously
		send_booking_confirmation_email.delay(booking.user.email, booking.id)