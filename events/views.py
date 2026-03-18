from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Event, Booking
from .serializers import EventSerializer, BookingSerializer

# ----------------------------
# Events
# ----------------------------
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])  # public GET
def event_list_create(request):
    """
    GET: List all events (public)
    POST: Create a new event (admin only, JWT required)
    """
    if request.method == 'GET':
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # JWT auth check
        if not request.user.is_authenticated:
            return Response({'error': 'Authentication required'}, status=401)
        # Admin check
        if not request.user.is_staff:
            return Response({'error': 'Only admins can create events'}, status=403)

        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])  # GET is public, PUT/DELETE require JWT + admin
def event_detail_update_delete(request, id):
    """
    GET: Retrieve a single event (public)
    PUT/DELETE: Admin only, JWT required
    """
    try:
        event = Event.objects.get(id=id)
    except Event.DoesNotExist:
        return Response({'error': 'Event not found'}, status=404)

    if request.method == 'GET':
        serializer = EventSerializer(event)
        return Response(serializer.data)

    elif request.method in ['PUT', 'DELETE']:
        # JWT auth check
        if not request.user.is_authenticated:
            return Response({'error': 'Authentication required'}, status=401)
        # Admin check
        if not request.user.is_staff:
            return Response({'error': 'Only admins can update/delete events'}, status=403)

        if request.method == 'PUT':
            serializer = EventSerializer(event, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            event.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


# ----------------------------
# Bookings
# ----------------------------
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])  # JWT required
def booking_list_create(request):
    """
    GET: List bookings for authenticated user
    POST: Create a booking for an event
    """
    if request.method == 'GET':
        bookings = Booking.objects.filter(user=request.user)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        event_id = request.data.get('event')
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response({'error': 'Event not found'}, status=404)

        # Check if event is full
        booked_count = Booking.objects.filter(event=event).count()
        if booked_count >= event.capacity:
            return Response({'error': 'Event is fully booked'}, status=400)

        serializer = BookingSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])  # JWT required
def booking_delete(request, pk):
    """
    DELETE: Delete a booking for the authenticated user
    """
    try:
        booking = Booking.objects.get(pk=pk, user=request.user)
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Booking.DoesNotExist:
        return Response({'error': 'Booking not found'}, status=404)