from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from sms.apis.models import Receipent


class Receipents(APIView):
    def save(self, request):
        data = request.data
        recipentData = Receipent.objects.create(data)
        return Response({"message": recipentData})
