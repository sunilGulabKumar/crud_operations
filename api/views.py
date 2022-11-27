from rest_framework.response import Response
from rest_framework.decorators import api_view
from rooms.serializers import ItemSerializers
from rooms.models import Item

@api_view(['GET'])
def getdata(request):
    item=Item.objects.all()
    serializers=ItemSerializers(item,many=True)
    return Response(serializers.data)
    
@api_view(['POST'])
def addview(request):
    serializers=ItemSerializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)
