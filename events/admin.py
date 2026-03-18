from django.contrib import admin
from .models import Event, Booking

# Register models so they appear in admin
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'capacity')
    search_fields = ('title', 'location')
    list_filter = ('date',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'booked_at')
    list_filter = ('booked_at',)