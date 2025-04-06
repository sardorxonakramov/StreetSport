
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
# from rest_framework.authentication import authenticate
import rest_framework
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: HttpResponse("Xush kelibsiz!"), name='home'),
    path('api/v1/auth', include('rest_framework.urls')),
    path('api/v1/', include('USERS.urls')),

]
