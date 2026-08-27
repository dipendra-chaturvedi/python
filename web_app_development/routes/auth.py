from flask import Blueprint, render_template, request, redirect, url_for, flash, session

auth_bp = Blueprint(
    "auth",
    __name__
)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "1234":

            session["user"] = username

            flash("Login successful")

            return redirect(
                url_for("employee.employee")
            )

        flash("Invalid username or password")

    return render_template("login.html")

@auth_bp.route("/logout")
def logout():

    session.pop("user", None)

    flash("Logout successful")

    return redirect(
        url_for("auth.login")
    )