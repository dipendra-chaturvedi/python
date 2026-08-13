from flask import Flask, request

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data["username"]
    password = data["password"]

    if username == "admin" and password == "1234":
        return {
            "message": "Login successful"
        }, 200

    return {
        "message": "Invalid username or password"
    }, 401


if __name__ == "__main__":
    app.run(debug=True)