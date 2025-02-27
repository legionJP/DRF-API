from django.shortcuts import render
from rest_framework import generics
from .models import User , Menuitem , Order, OrderItem , Cart, Category

# Create your views here.

# User registration and token generation view

class User(generics.ListCreateAPIView):
    queryset = User.objects.get_all()
