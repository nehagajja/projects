from django.db import models

class Product(models.Model):
    Product_ID=models.IntegerField()
    category_id=models.IntegerField()
    Title=models.CharField(max_length=50)
    Description=models.CharField(max_length=100)
    Price=models.FloatField()
    Status=models.CharField(max_length=20)
    created_at=models.TimeField()
    updated_at=models.TimeField()
    Expiry_date=models.TimeField()


class Category(models.Model):
    category_id=models.IntegerField()
    Name=models.CharField(max_length=50)
