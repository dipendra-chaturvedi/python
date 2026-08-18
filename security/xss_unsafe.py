from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    name = request.args.get("name", "")

    return f"<h2>Hello {name}</h2>"


app.run(debug=True)