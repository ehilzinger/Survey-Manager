from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status

from ..serializers import OrganizationSerializer

class OrganizationView(generics.ListCreateAPIView):
    def post(self, request, *args, **kwargs):
        if not request.user.profile.can_create_org:
            return Response(data={
                'message':'Not Authorized'
            }, status=status.HTTP_403_FORBIDDEN)
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
    def get(self, request, *args, **kwargs):
        return Response(data=OrganizationSerializer(request.user.profile.org).data, status=status.HTTP_200_OK)