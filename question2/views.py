from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Slot
from .serializer import SlotSerializer

# Create your views here.


class BookingView(APIView):
    """View for retrieving list of bookings and for booking new slots"""

    model = Slot
    serializer = SlotSerializer

    def get(self, request):
        """Returns list of all previous booking"""

        bookings = self.model.objects.all()
        serializer = self.serializer(bookings, many=True)

        return Response(serializer.data)

    def post(self, request):
        """Books a new slots if possible"""

        slot_number = request.data.get("slot")
        name = request.data.get("name")

        slot = self.model.book(slot_number, name)
        if slot:
            return Response({
                "status": f"Confirmed booking for {name} in slot {slot_number}"
            })

        return Response({
            "status": f"Slot full, unable to save booking for {name} in slot {slot_number}"
        })


class CancelView(APIView):
    """View for canceling a booking, if possible"""

    model = Slot

    def post(self, request):
        slot_number = request.data.get("slot")
        name = request.data.get("name")

        if self.model.cancel(slot_number, name):
            return Response({
                "status": f"Canceled booking for {name} in slot {slot_number}"
            })

        return Response({
            "status": f"No booking for the name {name} in slot {slot_number}"
        })
