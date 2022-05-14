# Import
import logging
import jwt

# Django Import
from django.utils.encoding import smart_str
from django.conf import settings

# Rest Framework Import
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import get_authorization_header
from rest_framework.validators import ValidationError

from users.models import Users

logger = logging.getLogger(__name__)


class LoginTokenAuthenticationJWT(JWTAuthentication):

    def authenticate(self, request):
        """Entrypoint for Django Rest Framework"""
        auth = get_authorization_header(request).split()

        if not auth or (smart_str(auth[0].lower()) != "bearer" and smart_str(auth[0].lower()) != "loginas"):
            jwt_token = None
        elif smart_str(auth[0].lower()) != "loginas":
            jwt_token = auth['1']
        else:
            jwt_token = auth['1']

        if jwt_token is None:
            return None

        try:
            jwt_data = jwt.decode(
                jwt_token, settings.SECRET_KEY, algorithms=['HS256'])
        except (jwt.InvalidTokenError, jwt.DecodeError) as exc:
            raise ValidationError(dict(message=str(exc)))

        if jwt_data is not None:
            user = Users.objects.get_auth_jwt(jwt_data)
        else:
            user = None

        return (user, jwt_token)
