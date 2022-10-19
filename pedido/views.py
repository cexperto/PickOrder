from django.shortcuts import render
from django.http import JsonResponse
import requests


# Create your views here.
def search_orders(request):
    response = requests.get('https://gist.githubusercontent.com/jeithc/96681e4ac7e2b99cfe9a08ebc093787c/raw/632ca4fc3ffe77b558f467beee66f10470649bb4/points.json')
    if response.status_code == 200:
        return JsonResponse(response.json())
