from flask import Flask, request

app = Flask(__name__)


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data:
        return {"message": "JSON data is required"}, 400

    username = data.get("username")
    age = data.get("age")

    if not username or not username.strip():
        return {"message": "Username is required"}, 400

    if not isinstance(age, int):
        return {"message": "Age must be a number"}, 400

    if age < 18:
        return {"message": "Age must be 18 or above"}, 400

    return {
        "message": "Registration data is valid",
        "username": username,
        "age": age
    }, 200


app.run(debug=True)