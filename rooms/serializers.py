from rest_framework import serializers
#from rooms.serializers import ItemSerializers
from rooms.models import Item

class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields='__all__'