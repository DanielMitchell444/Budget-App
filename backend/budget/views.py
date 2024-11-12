from django.shortcuts import render
from rest_framework import viewsets
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSeralizers
from .forms import UserForm
from rest_framework import status

from .models import Users
from django.shortcuts import render
from django import forms
from .serializers import LoginSeralizer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = UserSeralizers
    queryset = Users.objects.all()
@api_view(['POST'])
def api_register_user(request):
    serializer = UserSeralizers(data=request.data)  
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response({'status': 'error', 'errors': serializer.errors}, status=400)
@csrf_exempt
def login_user(request):

    serializer = LoginSeralizer(data=request.data)
    if not serializer.is_valid():
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    username = serializer.validated_data["Username"]
    password = serializer.validated_data["Password"]
    user = authenticate(username=username, password=password)

    if user:
        return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid username or password."}, status=status.HTTP_401_UNAUTHORIZED)