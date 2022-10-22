from turtle import pd
import requests


class FindDriver:
    def search_orders(self, url, id_driver):
        self.url = url
        response = requests.get(url)
        if response.status_code == 200:
            response_list = response.json()["alfreds"]
            _find_driver = self.find_driver(response_list, id_driver)
            return _find_driver
        return False

    def find_driver(self, _list, driver):
        find_driver = [x for x in _list if x["id"] == driver]
        if len(find_driver) > 0:
            return True
        return False
