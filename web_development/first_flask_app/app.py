from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>My Web App</title>
        </head>

        <body>
            <h1>Hello Dipendra</h1>
            <p>This page is coming from Flask.</p>
        </body>
    </html>
    """


app.run(debug=True)