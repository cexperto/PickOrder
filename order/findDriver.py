import requests


class FindDriver:
    def search_orders(self, url, id_driver):
        self.url = url
        response = requests.get(url)
        if response.status_code == 200:
            response_list = response.json()['alfreds']
            _find_driver = self.find_driver(response_list, id_driver)
            return _find_driver
        return False

    def find_driver(self, _list, driver):
        find_driver = [x for x in _list if x['id']==driver]
        if len(find_driver)>0:
            return True
        return False

# find = FindDriver()
# url = 'https://gist.githubusercontent.com/jeithc/96681e4ac7e2b99cfe9a08ebc093787c/raw/632ca4fc3ffe77b558f467beee66f10470649bb4/points.json'
# print(find.search_orders(url, 1))
