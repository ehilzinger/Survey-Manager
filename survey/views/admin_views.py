from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import exceptions, permissions, generics
from rest_framework.views import status
from rest_framework.response import Response

from ..serializers import UserSerializer

class GetUserDetailView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        return Response(data={'username': request.user.username}, status=status.HTTP_200_OK)

class RegisterUserView(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'message': 'Created User'}, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)