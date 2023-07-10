from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.serializers import ValidationError
from .models import Weather

class RegistrationSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=150)
    password=serializers.CharField(max_length=150,write_only=True)

    def validate_username(self,value):
        if User.objects.filter(username=value).exists():
            raise serializers.validationError({'msg':'username already exist'})
        return value

    def create(self,validated_data):
        username=validated_data.get('username')
        password=validated_data.get('password')

        user=User.objects.create_user(username=username,password=password)
        return user


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['location', 'temperature', 'humidity', 'timestamp']