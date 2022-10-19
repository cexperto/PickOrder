from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from order.models import Order
from order.serializers import OrderSerializer

# Create your views here.
def search_orders(request):
    url = 'https://gist.githubusercontent.com/jeithc/96681e4ac7e2b99cfe9a08ebc093787c/raw/632ca4fc3ffe77b558f467beee66f10470649bb4/points.json'
    response = requests.get(url)
    if response.status_code == 200:
        return JsonResponse(response.json())


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer