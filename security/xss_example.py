from flask import Flask, request, render_template_string

app = Flask(__name__)


@app.route("/")
def home():
    name = request.args.get("name", "")

    return render_template_string(
        "<h2>Hello {{ name }}</h2>",
        name=name
    )


app.run(debug=True)