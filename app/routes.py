from flask import render_template, flash, redirect
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
    if form.validate_on_submit():
        flash("Login request for user {} with {}, remember_me={}".format(
            form.username.data,
            form.password.data,
            form.remember_me.data))
        return redirect("/index")

    return render_template("login.html", title="Sign In", form=form)
