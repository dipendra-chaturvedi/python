import bcrypt

stored_username = "admin"

stored_password_hash = bcrypt.hashpw(
    "admin123".encode(),
    bcrypt.gensalt()
)


username = input("Username: ")
password = input("Password: ")


if username != stored_username:
    print("Invalid username")

elif bcrypt.checkpw(
    password.encode(),
    stored_password_hash
):
    print("Login successful")

else:
    print("Invalid password")