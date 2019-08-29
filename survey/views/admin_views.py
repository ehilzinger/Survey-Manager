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
        self.stdout.write('Created User')
        User.objects.create_user(
            username=request.data['username'], password=request.data['password'], email=request.data['email'])
        return Response(data={'message': 'Created User'}, status=status.HTTP_201_CREATED)
