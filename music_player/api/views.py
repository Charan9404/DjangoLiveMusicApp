from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics 
from .models import Room
from .serializers import RoomSerializer

# Create your views here.
#this will not only allow us to view a room but also create a room
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
