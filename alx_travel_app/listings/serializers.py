from rest_framework import serializers
from .models import Listing, Booking


class ListingSerializer(serializers.ModelSerializer):
    """Serialize Listing model"""
    class Meta:
        model = Listing
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    """Serialize Booking model"""
    # listing = ListingSerializer(read_only=True)  
    # listing_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Listing.objects.all(),
    #     source='listing',
    #     write_only=True,
    #     required=True
    # )

    class Meta:
        model = Booking
        fields = '__all__'
