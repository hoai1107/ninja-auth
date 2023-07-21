from ninja import Schema, ModelSchema
from django.contrib.auth.models import User


class JWTSchemaOut(Schema):
    access_token: str
    token_type: str


class SignupSchema(ModelSchema):
    class Config:
        model = User
        model_fields = ["username", "password", "email", "first_name", "last_name"]


class LoginSchema(Schema):
    username: str
    password: str
