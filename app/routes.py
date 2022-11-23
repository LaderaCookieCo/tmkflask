from app import app
from flask import render_template

@app.route("/")
def index():
    posts = [
        {"user": {"username": "Xx_potato_eater_xX}"},
        "body": "are you a potato"},
        {"user": {"username": "Former U.S. President Barack Obama"},
        "body": "My fellow Americans, let me be clear: The short form of racecar driver is not a racist."}
    ]
    return render_template("index.html", title = "Welcome to Bacefook", user = {"username": "David"}, posts = posts)