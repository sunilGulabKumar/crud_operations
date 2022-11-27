# from django.shortcuts import Response
# from django.shortcuts import 
from rest_framework.response import Response
# from .views import views
from rest_framework.decorators import api_view
from crud_operations.serializers import HotelBookSerializers
from crud_operations.models import HotelBook

# Create your views here.

@api_view(['GET'])
def helloworld(request):
    employee=HotelBook.objects.all()
    serializers=HotelBookSerializers(employee,many=True)
    return Response(serializers.data)

@api_view(['GET'])
def addview(request):
    serializers=HotelBookSerializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)
