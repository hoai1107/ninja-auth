from ninja import Router
from ninja.errors import AuthenticationError

from .schema import SignupSchema, LoginSchema, JWTSchemaOut
from .token import create_access_token, AuthBearer

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

router = Router()


@router.post("/signup")
def create_user(request, payload: SignupSchema):
    user = User.objects.create_user(**payload.dict())
    return {"msg": "Create user successfully"}


@router.post("/login", response=JWTSchemaOut)
def login(request, payload: LoginSchema):
    user = authenticate(username=payload.username, password=payload.password)
    if user is None:
        raise AuthenticationError

    jwt_token = create_access_token(user)
    return {"access_token": jwt_token, "token_type": "Bearer"}


@router.get("/bearer", auth=AuthBearer())
def test_bearer(request):
    return request.auth
