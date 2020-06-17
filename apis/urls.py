from django.urls import path

from .views import create_receipents_details, save_receipents_details, get_receipents_details

urlpatterns = [
    path('v1/sms/receipent/create', create_receipents_details),
    path('v1/sms/receipent/save', save_receipents_details),
    path('v1/sms/receipent/all', get_receipents_details),
]
