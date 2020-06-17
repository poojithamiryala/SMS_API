from django.http import JsonResponse

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Receipent
from .serializers import RecepientSerializer


@api_view(['GET'])
def get_receipents_details(request):
    if request.method == 'GET':
        receipents = Receipent.objects.filter()
        receipentData = RecepientSerializer(receipents, many=True)
        data = {
                    'message': 'Retreived token successfully',
                    'data': receipentData.data,
                    "status": status.HTTP_200_OK
        }
        return JsonResponse(data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_receipents_details(request):
    print(request.data)
    if request.method == 'POST':
        data = request.data
        serializer = RecepientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['PUT'])
def save_receipents_details(request):
    if request.method == 'PUT':
        Receipent.objects.filter(name=request.data['name']).update(email=request.data['email'],phone_number=request.data['phone_number'])
        receipent = Receipent.objects.get(name=request.data['name'])
        receipentData = RecepientSerializer(receipent, many=False).data
        data = {
            'message': 'Updated successfully',
            'data': receipentData,
            "status": status.HTTP_200_OK
        }
        return JsonResponse(data, status=status.HTTP_200_OK)
