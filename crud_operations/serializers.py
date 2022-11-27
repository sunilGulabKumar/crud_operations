from rest_framework import serializers 
from crud_operations.models import HotelBook 

class HotelBookSerializers(serializers.ModelSerializer):
    class Meta:
        model = HotelBook 
        fields = '__all__'