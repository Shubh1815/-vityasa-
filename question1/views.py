from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class PositiveIntegerStatsView(APIView):

    def post(self, request):
        """Calculate stats about positive integers in post data"""

        items = request.data 
        total_entries = len(items)

        # A item is valid if its a positive integer
        positive_integers = [item for item in items if isinstance(item, int) and item > 0]
        valid_entries = len(positive_integers)

        stats = {
            'valid_entries': valid_entries,
            'invalid_entries': total_entries - valid_entries,
            'min': min(positive_integers),
            'max': max(positive_integers),
            'average': round(sum(positive_integers) / valid_entries, 2)
        }

        return Response(stats)
