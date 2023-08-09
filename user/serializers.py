from django.contrib.auth.hashers import make_password
from rest_framework import serializers, status
from rest_framework.validators import ValidationError

from .models import User


class UserSignupSerializer(serializers.Serializer):
    guid = serializers.CharField(read_only=True, source="guid.hex")
    email = serializers.EmailField(allow_blank=False)
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = User.objects.filter(email=attrs.get("email")).exists()
        if email:
            raise ValidationError(
                detail="User with email exists", code=status.HTTP_403_FORBIDDEN
            )
        return super().validate(attrs)

    def create(self, validated_data):
        if validated_data.get("password") != validated_data.pop("confirm_password"):
            raise ValidationError(
                detail="Confirm password doesn't match", code=status.HTTP_403_FORBIDDEN
            )
        else:
            new_user = User(**validated_data)
            new_user.password = make_password(validated_data.get("password"))
            new_user.save()
            return new_user
