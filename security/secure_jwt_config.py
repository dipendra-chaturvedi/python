import os

secret_key = os.getenv("SECRET_KEY")

if not secret_key:
    raise ValueError("SECRET_KEY environment variable is not set")

print("JWT secret loaded successfully")
print(secret_key)