from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    re_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "re_password"]

    def validate(self, data):
        if data.get("password") != data.get("re_password"):
            raise serializers.ValidationError("message : password fields didn't match")
        return data

    def create(self, validated_data):
        email = validated_data.get("email")
        password = validated_data.get("password")
        user = User(email=email)
        user.set_password(password)

        user.save()
        return user


class UserInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
