from app import app


@app.route("/")
def index():
    return '<img src="https://media.tenor.com/pJ3GkVJYxUEAAAAC/duck-spinning.gif">' 