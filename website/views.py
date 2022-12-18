from flask import Blueprint, render_template, request, flash

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def homepage():
    return render_template("home.html")

@views.route("/history")
def historia():
    return render_template("historia.html")

@views.route("/crie", methods=['GET', 'POST'])
def create_post():
    if request.method == "POST":
        text = request.form.get('text')
        if not text:
            flash('Post não pode estar vazio', category='error')
    return render_template('create_post.html')