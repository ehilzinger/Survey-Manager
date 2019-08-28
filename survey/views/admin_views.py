from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import exceptions, permissions, generics
from rest_framework.views import status
from rest_framework.response import Response

class GetUserDetailView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        return Response(data={'username': request.user.username}, status=status.HTTP_200_OK)