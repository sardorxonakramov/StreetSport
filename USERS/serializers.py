from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers



User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, min_length=6)
    password2 = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'password1', 'password2']
        extra_kwargs = {
            'password1': {'write_only': True},
            'password2': {'write_only': True}
        }

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Parollarni bir xil kiritmadingiz")
        return data

    def create(self, validated_data):
        password = validated_data.pop('password1')
        validated_data.pop('password2')  
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user



class LoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id",'email', 'first_name', 'last_name', 'phone', 'role']
        extra_kwargs = {'password': {'write_only': True}}
    def post(self):
        pass

class UserInfoSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'phone']
        extra_kwargs = {'password': {'write_only': True}}