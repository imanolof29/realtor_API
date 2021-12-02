from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from rest_framework import routers, urlpatterns
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls))
]