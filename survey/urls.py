from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .views import (GetUserDetailView, RegisterUserView, GetRefreshTokenLifetimeView)

AUTH_PATTERNS = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token-obtain'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token-refresh'),
    path('token/lifetime/', GetRefreshTokenLifetimeView.as_view(), name='token-lifetime'),
    path('userdetails/', GetUserDetailView.as_view(), name='user-detail')
]

urlpatterns = [
    path('auth/', include(AUTH_PATTERNS)),
    path('register/', RegisterUserView.as_view(), name='register-user')
]
