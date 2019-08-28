from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

AUTH_PATTERNS = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token-obtain'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token-refresh')
]

urlpatterns = [
    path('auth/', include(AUTH_PATTERNS))
]
