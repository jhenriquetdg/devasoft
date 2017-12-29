from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User


def so_name():
    import os

    serv_agent = ' '.join(os.uname())
    return [serv_agent]


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Zetdg"}
    posts = [
        {
            "author": {"username": "John"},
            "body": "Deus é forte!"
        },

        {
            "author": {"username": "Susan"},
            "body": "Cristo salva."
        }
    ]
    return render_template("index.html", title="Home", user=user, posts=posts, so_name=so_name())


@app.route("/login", methods=["GET", "POST"])
def login():
    """
        Login route.

        If is autenticated, go to index.
        If there is a submission
            Check if the user is ok, or restart login
            Check if the password is ok, or restart login

            All good?
                Mark as logged and log user in == AUTHENTICATED
    """
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    flash("Login...")

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None:
            flash("{} is an invalid username.".format(form.username.data))
            return redirect(url_for("login"))

        if not user.check_password(form.password.data):
            flash("{} is not the password of {} user ".format(
                form.password.data,
                form.username.data))
            return redirect(url_for("login"))

        login_user(user, remember=form.remember_me.data)

        return redirect(url_for("index"))

    return render_template("login.html", title="Sign In", form=form, so_name=so_name())
