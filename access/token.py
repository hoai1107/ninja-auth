import jwt
import os
from datetime import datetime, timedelta
from django.contrib.auth.models import User

from ninja.security import HttpBearer
from ninja.errors import AuthenticationError

SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        except jwt.exceptions.InvalidTokenError:
            raise AuthenticationError

        return payload


def create_access_token(user: User):
    payload = {
        "name": user.username,
        "role": "client",
        "exp": datetime.utcnow() + timedelta(hours=1),
    }

    jwt_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    print(jwt_token)
    return jwt_token
