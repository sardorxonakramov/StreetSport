from django.urls import path
from .views import (
    StadionBookingCreateView,
    ManagerStadionOfflineBookingView,
    PublicActiveStadionListView,
)

urlpatterns = [
    path("book/", StadionBookingCreateView.as_view(), name="stadion-book"),
    path(
        "book/offline/",
        ManagerStadionOfflineBookingView.as_view(),
        name="stadion-book-offline",
    ),
    path(
        "stadions/",
        PublicActiveStadionListView.as_view(),
        name="public-stadions",
    ),
]
