from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import Users


class RegisterSerializer(serializers.Serializer):

    email = serializers.EmailField(max_length=255)
    phone = serializers.CharField(max_length=20, allow_null=True, allow_blank=True, required=False)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, min_length=6)

    # class Meta:
    #     model = Users
    #     fields = (
    #         'id',
    #         'last_name',
    #         'first_name',
    #         'email',
    #         'phone',
    #         'password'
    #     )
    #     abstract = True


class LoginUserSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, min_length=6)

    # class Meta:
    #     model = Users
    #     fields = (
    #         'email',
    #         'password'
    #     )
    #     abstract = True
