from django.urls import re_path
from rest_framework_simplejwt import views

from .views import (
    MyTokenObtainPairView,
    Test
)

urlpatterns = [
    re_path(r"^jwt/create/?", MyTokenObtainPairView.as_view(), name="jwt-create"),
    re_path(r"^jwt/refresh/?", views.TokenRefreshView.as_view(), name="jwt-refresh"),
    re_path(r"^jwt/verify/?", Test.as_view(), name="jwt-verify"),
]
