import jwt
from datetime import datetime, timedelta, timezone


secret_key = "my-super-secret-jwt-key-1234567890"

payload = {
    "username": "admin",
    "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
}

# JWT Authentication
token = jwt.encode(
    payload,
    secret_key,
    algorithm="HS256"
)

print(token)

# Decode and verify the JWT
decoded_data = jwt.decode(
    token,
    secret_key,
    algorithms=["HS256"]
)

print(decoded_data)