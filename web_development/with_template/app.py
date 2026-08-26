from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/add", methods=["POST"])
def add_employee():

    name = request.form.get("name")
    salary = request.form.get("salary")

    if not name or not name.strip():
        return "Employee name is required", 400

    if not salary or not salary.isdigit():
        return "Salary must be a number", 400

    return redirect(
    url_for(
        "result",
        name=name,
        salary=salary
    )
)

@app.route("/result")
def result():
    name = request.args.get("name")
    salary = request.args.get("salary")

    return render_template(
        "result.html",
        name=name,
        salary=salary
    )


app.run(debug=True)