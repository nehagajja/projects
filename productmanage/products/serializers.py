from rest_framework import serializers
from . import models

class Productserializer(serializers.ModelSerializer):
    class Meta():
        model=models.Products
        fields="__all__"#to get all the fields

class Categoryserializer(serializers.ModelSerializer):
    class Meta():
        model2=models.Category
        fields="__all__"#to get all the fields
