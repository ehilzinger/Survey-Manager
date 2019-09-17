from django.db import IntegrityError, transaction
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status, APIView

from ..serializers import SurveyBaseSerializer
from ..models import SurveyBase


class SurveyBaseView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            serializer = SurveyBaseSerializer(
                data=request.data)
            if serializer.is_valid():
                serializer.save(survey_owner_user=request.user.profile, survey_owner_org=request.user.profile.org)
                return Response(status=status.HTTP_201_CREATED)
            return Response(data=serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except IntegrityError as e:
            transaction.rollback()
            return Response(data=e.args, status=status.HTTP_400_BAD_REQUEST)
