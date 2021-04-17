from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class PointView(APIView):

    def post(self, request):
        x = request.data.get('x')
        y = request.data.get('y')

        square_points = request.session.get('square_points', None)

        if square_points:
            p1, p2, p3, p4 = map(tuple, square_points)
            return Response({
                "status": f"Success {p1} {p2} {p3} {p4}"
            })

        points = request.session.get('points', list())
        points.append((x, y))

        points_set = set(map(tuple, points))
        points_set.add((x, y))
        
        total_points = len(points_set)
        points = sorted(points_set)

        request.session['points'] = points

        for i in range(total_points):
            p1 = points[i]
            for j in range(i + 1, total_points):
                p2 = points[j]

                length = p2[0] - p1[0]
                width = p2[1] - p1[1]

                # If length is equal to width then Square
                if abs(length) == abs(width):  
                    p3 = (p2[0], p2[1] - width)
                    p4 = (p2[0] - length, p2[1])
    
                    if p3 in points and p4 in points_set:

                        request.session['square_points'] = (p1, p2, p3, p4)

                        return Response({
                            "status": f"Success {p1} {p2} {p3} {p4}"
                        })

        return Response({"status": "accepted"})
