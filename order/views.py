from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

from rest_framework import generics
from order.models import Order
from order.serializers import OrderSerializer
from order.DistanceBetwenTwoPoints import DistanceBetwenTwoPoints


# Create your views here.
class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderByDate(generics.ListAPIView):
    queryset = Order.objects.all().order_by("hour")
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["date_order", "driver"]


@api_view(["POST"])
def find_driver(request):
    if request.method == "POST":
        if (
            request.data["date_order"]
            and request.data["hour"]
            and request.data["latitud"]
            and request.data["longitude"]
        ):
            lat1 = request.data["latitud"]
            long1 = request.data["longitude"]
            date_order = request.data["date_order"]
            hour = request.data["hour"]
            url = "https://gist.githubusercontent.com/jeithc/96681e4ac7e2b99cfe9a08ebc093787c/raw/632ca4fc3ffe77b558f467beee66f10470649bb4/points.json"
            r = requests.get(url)
            data_drivers = r.json()["alfreds"]
            query_drivers = list(
                Order.objects.all()
                .filter(date_order=date_order)
                .exclude(hour=hour)
                .values("driver")
            )
            ids_drivers = []
            disp_drivers = []
            for i in query_drivers:
                ids_drivers.append(int(i.get("driver")))

            for i in data_drivers:
                if i["id"] in ids_drivers:
                    disp_drivers.append(i)
            return search_driver_nearly(disp_drivers, lat1, long1)
        return Response({"error": "invalid keys"})


def search_driver_nearly(json_data_drivers, lat1, long1):
    locations = []
    find_distance = DistanceBetwenTwoPoints()
    for drivers in json_data_drivers:
        f_d = find_distance.calculate_distance(
            float(lat1), float(drivers["lat"]), float(long1), float(drivers["lng"])
        )
        result = (drivers["id"], f_d)
        locations.append(result)

    search_distance = min([x[1] for x in locations])
    min_distance = [x for x in locations if x[1] == search_distance]
    return Response(
        {
            "driver more nearly": {
                "id": min_distance[0][0],
                "distance": min_distance[0][1],
            }
        }
    )
