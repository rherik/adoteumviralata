from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def homepage():
    return render_template("home.html")

@views.route("/history")
def historia():
    return render_template("historia.html")
