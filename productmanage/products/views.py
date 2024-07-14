from django.shortcuts import render
from .models import Product,Category
from .serializers import Productserializer
from .serializers import Categoryserializer
from rest_framework import viewsets

# Create your views here.
class Productview(viewsets.ModelViewSet):
    queryset=.objects.all()
    serializer_class=Productserializer

class Categoryview(viewsets.ModelViewSet):
    queryset=Vendor.objects.all()
    serializer_class=Categoryserializer


