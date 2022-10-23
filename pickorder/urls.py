from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from order import views
from order.views import OrderList, OrderByDate


schema_view = get_schema_view(
   openapi.Info(
      title="Pick order API",
      default_version='v1',
      description="Project to implement a system that allows clients to schedule, in a available time slots, when a driver can stop by and pick up an ordern",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="andresayaladev@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


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

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
