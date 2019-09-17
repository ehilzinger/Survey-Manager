from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .views import (RegisterUserView, OrganizationView, SurveyBaseView, UpdateUserView)

AUTH_PATTERNS = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token-obtain'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token-refresh'),
]

ORG_PATTERNS = [
    path('organization/', OrganizationView.as_view(), name='org-list')
]

SURVEY_PATTERNS = [
    path('surveybase/', SurveyBaseView.as_view(), name='survey-base')
]

urlpatterns = [
    path('auth/', include(AUTH_PATTERNS)),
    path('org/', include(ORG_PATTERNS)),
    path('survey/', include(SURVEY_PATTERNS)),
    path('register/', RegisterUserView.as_view(), name='register-user'),
    path('user/', UpdateUserView.as_view(), name='update-user')
]
