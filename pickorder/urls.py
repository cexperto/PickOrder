"""pickorder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from order import views
from order.views import OrderList, OrderByDate


def index(request):
    return HttpResponse('pick orders API')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('api-auth/', include('rest_framework.urls')),
    # path('driver', views.search_orders, name='driver'),
    path('order', OrderList.as_view(), name='order'),
    path('orderbydate', OrderByDate.as_view(), name='orderbydate'),
    path('drivernear', views.find_driver, name='drivernear'),
]
