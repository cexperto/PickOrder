from django.test import TestCase
from order.models import Order
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from order.findDriver import FindDriver
from order.validateHour import ValidateHour
import json


class OrderTestCase(APITestCase):
    def test_model_order(self):
        order = Order(
            id=1,
            latitud_collected=20,
            longitud_collected=25,
            latitud_destiny=40,
            longitud_destiny=45,
            date_order="2022-10-21",
            hour="8:00",
            driver=2,
        )
        self.assertIs(order.driver, 2)

    def test_create_order_succes(self):
        data = {
            "latitud_collected": 20,
            "longitud_collected": 25,
            "latitud_destiny": 40,
            "longitud_destiny": 45,
            "date_order": "2022-10-21",
            "hour": "8:00",
            "driver": 1,
        }
        response = self.client.post(reverse("order"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["id"], 1)

    def test_create_order_faill(self):
        data = {
            "latitud_collected": 20,
            "longitud_collected": 25,
            "latitud_destiny": 40,
            "longitud_destiny": 45,
            "date_order": "2022-10-21",
            "hour": "8:00",
            "driver": 50,
        }
        response = self.client.post(reverse("order"), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data[0].code, "invalid")

    def test_get_order(self):
        order = Order(
            id=1,
            latitud_collected=20,
            longitud_collected=25,
            latitud_destiny=40,
            longitud_destiny=45,
            date_order="2022-10-21",
            hour="8:00",
            driver=2,
        )
        order.save()
        response = self.client.get(reverse("order"), format="json")
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data[0]["id"], 1)

    def test_order_by_date(self):
        order = Order(
            id=1,
            latitud_collected=20,
            longitud_collected=25,
            latitud_destiny=40,
            longitud_destiny=45,
            date_order="2022-10-21",
            hour="8:00",
            driver=1,
        )
        order2 = Order(
            id=2,
            latitud_collected=20,
            longitud_collected=25,
            latitud_destiny=40,
            longitud_destiny=45,
            date_order="2022-10-22",
            hour="8:00",
            driver=1,
        )
        order3 = Order(
            id=3,
            latitud_collected=20,
            longitud_collected=25,
            latitud_destiny=40,
            longitud_destiny=45,
            date_order="2022-10-22",
            hour="9:00",
            driver=1,
        )

        order.save()
        order2.save()
        order3.save()
        data = {"date_order": "2022-10-22"}
        response = self.client.get(reverse("orderbydate"), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        data = {"date_order": "2022-10-22"}
        response = self.client.get(reverse("orderbydate"), data=data)


class TestFindDriver(TestCase):
    url = "https://gist.githubusercontent.com/jeithc/96681e4ac7e2b99cfe9a08ebc093787c/raw/632ca4fc3ffe77b558f467beee66f10470649bb4/points.json"
    search_order = FindDriver()
    data = [
        {"id": 9, "lat": "9", "lng": "13", "lastUpdate": "2021-12-10T00:00:00.000Z"},
        {"id": 10, "lat": "10", "lng": "14", "lastUpdate": "2021-12-10T00:00:00.000Z"},
    ]

    def test_search_orders_true(self):
        search = self.search_order.search_orders(self.url, 1)
        self.assertEqual(search, True)

    def test_search_orders_false(self):
        search = self.search_order.search_orders(self.url, 50)
        self.assertEqual(search, False)

    def test_find_driver_true(self):
        search = self.search_order.find_driver(self.data, 9)
        self.assertEqual(search, True)

    def test_find_driver_false(self):
        search = self.search_order.find_driver(self.data, 50)
        self.assertEqual(search, False)


class TestValidateHour(TestCase):
    validate_hour = ValidateHour()

    def test_validate_hour_false(self):
        validate_hour = self.validate_hour.validateHour("as:as")
        self.assertEqual(validate_hour, False)

    def test_validate_hour_true(self):
        validate_hour = self.validate_hour.validateHour("8:00")
        self.assertEqual(validate_hour, True)
