from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User


class TokenSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True
    )

    confirmation_code = serializers.CharField(
        required=True
    )


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)
