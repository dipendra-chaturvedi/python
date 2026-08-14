from functools import wraps
from flask import request
import jwt

secret_key = "my-super-secret-jwt-key-1234567890"


def token_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return {
                "message": "Token is required"
            }, 401

        token = auth_header.replace("Bearer ", "")

        try:
            decoded_data = jwt.decode(
                token,
                secret_key,
                algorithms=["HS256"]
            )

        except jwt.ExpiredSignatureError:
            return {
                "message": "Token expired"
            }, 401

        except jwt.InvalidTokenError:
            return {
                "message": "Invalid token"
            }, 401

        return func(decoded_data, *args, **kwargs)

    return wrapper