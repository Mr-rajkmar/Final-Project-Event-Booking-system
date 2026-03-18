from django.urls import path
from . import views

urlpatterns = [
    # Events
    path('events/', views.event_list_create, name='event-list-create'),             # GET/POST all events
    path('events/<int:id>/', views.event_detail_update_delete, name='event-detail'), # GET/PUT/DELETE single event

    # Bookings
    path('bookings/', views.booking_list_create, name='booking-list-create'),       # GET/POST bookings
    path('bookings/<int:pk>/', views.booking_delete, name='booking-delete'),        # DELETE booking
]