import secrets

token = secrets.token_urlsafe(32)

print("Secure token:")
print(token)