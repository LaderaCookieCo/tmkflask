from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@app.route("/index")
@app.route("/")
def index():
    posts = [
        {"user": {"username": "Xx_potato_eater_xX"},
        "body": "are you a potato"},
        {"user": {"username": "Former U.S. President Barack Obama"},
        "body": "i'm hate twitter"}
    ]
    return render_template("index.html", title = "Welcome to Nowhere", user = {"username": "David"}, posts = posts)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'login requested for user {form.username.data}')
        return redirect(url_for("index"))
    return render_template('login.html', title = 'Sign In', form = form)
    