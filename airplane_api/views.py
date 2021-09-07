# from django.shortcuts import render
from rest_framework import generics
from .serializers import AirplanesSerializer
from .models import Airplane
from .permissions import IsOwnerOrReadOnly
# Create your views here.

class AirplanesList(generics.ListCreateAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplanesSerializer

class AirplanesDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Airplane.objects.all()
    serializer_class = AirplanesSerializer