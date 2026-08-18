from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

app.config["SECRET_KEY"] = "temporary-secret-key"

csrf = CSRFProtect(app)


@app.route("/")
def home():
    return {
        "message": "CSRF protection enabled"
    }

@app.route("/update-profile", methods=["POST"])
def update_profile():
    return {
        "message": "Profile updated"
    }

app.run(debug=True)