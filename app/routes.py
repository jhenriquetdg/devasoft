from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


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
    return render_template("index.html", title="Home", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    flash("Login...")
    if form.validate_on_submit():
        flash("succeed ")
        flash("Login request for user {} with {}, remember_me={}".format(
            form.username.data,
            form.password.data,
            form.remember_me.data))
        return redirect(url_for("index"))
    else:
        flash("form.")

    return render_template("login.html", title="Sign In", form=form)
