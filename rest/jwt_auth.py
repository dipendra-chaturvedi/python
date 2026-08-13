from flask import Flask, request
import jwt
from datetime import datetime, timedelta, timezone

app = Flask(__name__)

secret_key = "my-super-secret-jwt-key-1234567890"


@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data["username"]
    password = data["password"]

    if username != "admin" or password != "1234":
        return {
            "message": "Invalid username or password"
        }, 401

    payload = {
        "username": username,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
    }

    token = jwt.encode(
        payload,
        secret_key,
        algorithm="HS256"
    )

    return {
        "message": "Login successful",
        "token": token
    }, 200

@app.route("/profile", methods=["GET"])
def profile():

    token = request.headers.get("Authorization")

    if not token:
        return {
            "message": "Token is required"
        }, 401

    try:
        decoded_data = jwt.decode(
            token,
            secret_key,
            algorithms=["HS256"]
        )

        return {
            "message": "Access granted",
            "username": decoded_data["username"]
        }, 200

    except jwt.ExpiredSignatureError:
        return {
            "message": "Token expired"
        }, 401

    except jwt.InvalidTokenError:
        return {
            "message": "Invalid token"
        }, 401

if __name__ == "__main__":
    app.run(debug=True)