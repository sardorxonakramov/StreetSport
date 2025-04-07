from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model



User = get_user_model()

class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'password1','password2']
        extra_kwargs = {'password': {'write_only': True}}

class LoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id",'email', 'first_name', 'last_name', 'phone', 'role']
        # extra_kwargs = {'password': {'write_only': True}}

class UserInfoSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'phone']
        extra_kwargs = {'password': {'write_only': True}}