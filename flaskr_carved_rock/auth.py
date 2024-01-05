import functools

from flask import abort
from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from is_safe_url import is_safe_url
from urllib.parse import urlparse

from flaskr_carved_rock.db import get_db
from flaskr_carved_rock.models import User
from flaskr_carved_rock.sqla import sqla
from flask_login import login_user, current_user

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/register", methods=("GET", "POST"))
def register():
    """Register a new user.

    Validates that the username is not already taken. Hashes the
    password for security.
    """
    if request.method == "POST":
        try:
            user = User(username=request.form["username"], password=request.form["password"])
        except ValueError as e:
            flash(str(e))
            return render_template("auth/register.html")

        sqla.session.add(user)
        sqla.session.commit()
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html")


@bp.route("/login", methods=("GET", "POST"))
def login():
    """Log in a registered user by adding the user id to the session."""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        error = None
        user = User.query.filter_by(username=username).first()

        if user is None:
            error = "Incorrect username."
        elif not user.correct_password(password):
            error = "Incorrect password."

        if error is None:
            login_user(user)

            next = request.args.get('next')
            if next:
                if not is_safe_url(next, { urlparse(request.base_url).netloc }):
                    return abort(400)

            return redirect(next or url_for("index"))

        flash(error)

    return render_template("auth/login.html")


@bp.route("/logout")
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    return redirect(url_for("index"))
