from django.urls import path
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from .views import UserDetailView, UserListView



urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserListView.as_view(), name = 'user-list'),
    #no funciona
    path('users/<int:user_id>', UserDetailView.as_view(), name = 'user-detail')
]