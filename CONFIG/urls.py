from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    # JWT auth endpointlari
    path("api/v1/tokens/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("api/v1/logout/", TokenBlacklistView.as_view(), name="token_blacklist"),
    # my apps urls
    path("", lambda request: HttpResponse("Xush kelibsiz!"), name="home"),
    path("api/v1/auth", include("rest_framework.urls")),
    path("api/v1/", include("USERS.urls")),
    path("api/v1/", include("STADIUMS.urls")),
    path("api/v1/user/", include('BOOKING.urls'))
]
