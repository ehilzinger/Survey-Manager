from datetime import timedelta
from django.contrib.auth.models import User
from django.db import IntegrityError, transaction
from rest_framework import exceptions, permissions, generics
from rest_framework.views import status
from rest_framework.response import Response
from decouple import config

from ..serializers import UserSerializer
import logging

logger = logging.getLogger(__name__)
refresh_token_lifetime = timedelta(days=config('REFRESH_TOKEN_LIFETIME', default=1, cast=int))

class GetUserDetailView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        return Response(data={'username': request.user.username}, status=status.HTTP_200_OK)

class GetRefreshTokenLifetimeView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        return Response(data={'refresh_token_lifetime': refresh_token_lifetime}, status=status.HTTP_200_OK)

class RegisterUserView(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        try:
            User.objects.create_user(
                username=request.data['username'], password=request.data['password'], email=request.data['email'])
            logger.info('Created User')
            return Response(data={'message': 'Created User'}, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            transaction.rollback()
            if('unique constraint' in e.args[0].lower()):
                return Response(data={'message': 'Username is already taken'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response(data=e.args, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UpdateUserView(generics.UpdateAPIView):
    def put(self, request, *args, **kwargs):
        if(request.user is None):
            return Response(status=status.HTTP_403_FORBIDDEN)
        email = request.data['email']
        user = request.user
        if email is not None or not '':
            user.email = email
        user.save()
        return Response(status=status.HTTP_200_OK)
