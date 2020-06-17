from django.http import JsonResponse

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Receipent
from .serializers import RecepientSerializer


@api_view(['POST'])
def create_receipents_details(request):
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
        receipent = Receipent.objects.get(name=request.data.name)
        if receipent:
            try:
                receipentData = RecepientSerializer(receipent, many=False).data
                receipentData.save()
                data = {
                    'message': 'Retreived token successfully',
                    'data': receipentData,
                    "status": status.HTTP_200_OK
                }
                return JsonResponse(data, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                res = {'error': e, status: status.HTTP_403_FORBIDDEN}
                return JsonResponse(res, status=status.HTTP_403_FORBIDDEN)
        else:
            res = {
                'error': 'There is no recipent with this name', status: status.HTTP_400_BAD_REQUEST}
            return JsonResponse(res, status=status.HTTP_400_BAD_REQUEST)
