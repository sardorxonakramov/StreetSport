from django.urls import path
from .views import UserListView , UserDetailView,UserRegisterView
urlpatterns = [
    path('users/', UserListView.as_view(), name='userlist'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('register/', UserRegisterView.as_view(), name='register'),
    # path('login/', UserLoginView.as_view(), name='login'),
    # path('user-info/', UserInfoView.as_view(), name='user-info'),
]