from flask import render_template, request, redirect, url_for
from flask_login import login_user

from app import app
from app.auth.models import User
from app.auth.forms import LoginForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("login.html",errorBlock="none", form = LoginForm())

    form = LoginForm(request.form)
    

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("login.html", form=form,errorDisplay="block",error = "No such username or password")


    login_user(user)
    return redirect("../")
