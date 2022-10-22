from rest_framework import serializers
from order.models import Order
from .findDriver import FindDriver
from .validateHour import ValidateHour


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        url = "https://gist.githubusercontent.com/jeithc/96681e4ac7e2b99cfe9a08ebc093787c/raw/632ca4fc3ffe77b558f467beee66f10470649bb4/points.json"
        id_driver = validated_data["driver"]
        hour = validated_data["hour"]
        date_order = validated_data["date_order"]
        validate_hour = ValidateHour()
        if not validate_hour.validateHour(hour):
            raise serializers.ValidationError(
                "Hour field have incorrect format, should be hh:mm, in 24h, in range 8:00 to 18:00"
            )
        validate_calendar = self.validateCalendar(id_driver, date_order, hour)
        if not validate_calendar:
            raise serializers.ValidationError(
                "Driver is busy in selected hour, please select other"
            )
        find = FindDriver()
        if find.search_orders(url, int(id_driver)):
            return Order.objects.create(**validated_data)
        raise serializers.ValidationError("driver dont found")

    def validateCalendar(self, id_driver, date_order, hour):
        query = (
            Order.objects.filter(driver=id_driver)
            .filter(date_order=date_order)
            .filter(hour=hour)
        )
        if len(query) == 0:
            return True
        return False
