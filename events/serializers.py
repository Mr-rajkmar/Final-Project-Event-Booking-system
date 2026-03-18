from rest_framework import serializers
from .models import Event, Booking

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())  # auto assign logged-in user

    class Meta:
        model = Booking
        fields = '__all__'