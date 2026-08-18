from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for all routes
# CORS(app)

# Enable CORS for specific origins
CORS(app, origins=["http://localhost:3000"])


@app.route("/data")
def data():
    return {
        "message": "CORS enabled"
    }


app.run(debug=True)