from django.urls import path

from . import views

urlpatterns = [
    path('iotdata/', views.device_data, name='device_data'),
]