from rest_framework import serializers
from order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    
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

#     def create(self, validated_data):        
#         return Order.objects.create(**validated_data)

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