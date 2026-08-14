import hashlib

password = "admin123"

hashed_password = hashlib.sha256(
    password.encode()
).hexdigest()

print(hashed_password)