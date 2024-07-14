from rest_framework import serializers
from . import models

class vendorserializer(serializers.ModelSerializer):
    class Meta():
        model=models.Products
        model2=models.Category
        fields="__all__"#to get all the fields
