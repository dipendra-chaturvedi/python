from functools import wraps
from flask import session, flash, redirect, url_for


def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if "user" not in session:
            flash("Please login first")
            return redirect(
                url_for("auth.login")
            )

        return func(*args, **kwargs)

    return wrapper