from flask import Flask, render_template

from website.config import APP_NAME


app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "index.html",
        name=APP_NAME
    )


@app.route("/register")
def register():
    return render_template(
        "register.html"
    )


@app.route("/login")
def login():
    return render_template(
        "login.html"
    )


@app.route("/premium")
def premium():
    return render_template(
        "premium.html"
    )


@app.route("/support")
def support():
    return render_template(
        "support.html"
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
