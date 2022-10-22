from math import sqrt


class DistanceBetwenTwoPoints:
    def calculate_distance(self, lat1, lat2, long1, long2):
        distance = (lat1 - lat2) ** 2 + (long1 - long2) ** 2
        return sqrt(distance)
