from django.db import IntegrityError
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status

from ..models import SurveyBase

class SurveyBaseView(generics.ListCreateAPIView):
    def post(self, request, *args, **kwargs):
        try:
            SurveyBase.objects.create(
                survey_title=request.data['survey_title'],
                survey_description=request.data['survey_description'],
                survey_owner_org=request.user.profile.org,
                survey_owner_user=request.user,
                survey_approval_required=request.data['survey_approval_required'],
                survey_due_date=request.data['survey_due_date'],
                survey_creation_date=request.data['survey_creation_date'],
                survey_responsible_users=request.data['survey_responsible_users'],
                survey_archived=request.data['survey_archived']
            )
            return Response(status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            return Response(data=e.args, status=status.HTTP_400_BAD_REQUEST)

