from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from order.models import Order
from order.serializers import OrderSerializer

# Create your views here.
class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderByDate(generics.ListAPIView):
    queryset = Order.objects.all().order_by('hour')
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date_order','driver']