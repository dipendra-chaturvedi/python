import bcrypt

password = "admin123"

hashed_password = bcrypt.hashpw(
    password.encode(),
    bcrypt.gensalt()
)

entered_password = "admn123"

is_correct = bcrypt.checkpw(
    entered_password.encode(),
    hashed_password
)

print(is_correct)