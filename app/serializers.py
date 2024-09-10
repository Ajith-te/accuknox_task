from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, FriendRequest

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['email'] = validated_data['email'].lower()
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email').lower()
        password = data.get('password')
      

        user = authenticate(username=email, password=password)
        if not user:
             raise serializers.ValidationError("Invalid email or password.")
        
        data['user'] = user
        return data

class FriendRequestSerializer(serializers.ModelSerializer):
     class Meta:
        model = FriendRequest
        fields = ['to_user', 'status']
        read_only_fields = ['from_user']


class FriendRequestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ['to_user']
