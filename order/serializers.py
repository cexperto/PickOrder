from django.http import JsonResponse
from rest_framework import serializers
from rest_framework import status
from order.models import Order
import requests
from .findDriver import FindDriver

class OrderSerializer(serializers.ModelSerializer):
    hour = serializers.IntegerField(max_value=12)
    class Meta:
        model = Order
        fields = '__all__'

# class OrderSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     latitud = serializers.DecimalField(max_digits=22, decimal_places=16)
#     longitud = serializers.DecimalField(max_digits=22, decimal_places=16)
#     date_order = serializers.DateField()
#     hour_order = serializers.CharField(max_length=50)
#     driver = serializers.IntegerField()
    
    def create(self, validated_data):
        url = 'https://gist.githubusercontent.com/jeithc/96681e4ac7e2b99cfe9a08ebc093787c/raw/632ca4fc3ffe77b558f467beee66f10470649bb4/points.json'
        id_driver = validated_data['driver']
        find = FindDriver()
        if find.search_orders(url, id_driver):
            return Order.objects.create(**validated_data)
        raise serializers.ValidationError("driver dont found")
        

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.latitud = validated_data.get('latitud', instance.latitud)
#         instance.longitud = validated_data.get('longitud', instance.longitud)
#         instance.date_order = validated_data.get('date_order', instance.date_order)
#         instance.hour_order = validated_data.get('hour_order', instance.hour_order)
#         instance.driver = validated_data.get('driver', instance.driver)
#         instance.save()
#         return instance
