from django.urls import path
from . import views

urlpatterns = [
    path('pro', views.check, name='check'),
]