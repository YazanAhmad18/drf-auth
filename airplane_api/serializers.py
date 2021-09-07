from rest_framework import serializers
from .models import Airplane

class AirplanesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = ('id','type','description','author')