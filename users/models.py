# Django Import

from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser, UserManager

# Rest Framework Import
from rest_framework.validators import ValidationError


class AbstractUserManager(UserManager):

    def get_auth_jwt(self, jwt_data):
        user = self.filter(
            email=jwt_data['email'],
            is_deleted=False
        ).first()
        if user:
            if user.email is None:
                user.email = jwt_data['email']
                user.save()
                return user
            else:
                raise ValidationError(dict(
                    message="The username/password you've entered in incorrect, please try again."
                ))


class AbstractBaseUsers(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    password = models.CharField(max_length=255, null=True, unique=True)
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    object = AbstractUserManager()

    class Meta:
        abstract = True


class Users(AbstractBaseUsers):
    phone = models.CharField(max_length=255, null=True, default=None)
    email = models.CharField(max_length=255, null=True, default=None)
