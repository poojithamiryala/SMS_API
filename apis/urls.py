from django.urls import path

from .views import create_receipents_details, save_receipents_details

urlpatterns = [
    path('v1/sms/receipent/create', create_receipents_details),
    path('v1/sms/receipent/update', save_receipents_details),

]
