from flask import Flask
from routes.home import home_bp
from routes.auth import auth_bp
from routes.employee import employee_bp

app = Flask(__name__)

app.secret_key = "temporary-secret-key"

app.register_blueprint(home_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(employee_bp)


if __name__ == "__main__":
    app.run(debug=True)