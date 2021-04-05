from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact/")
def contact():
    return render_template("contacts.html")

@app.route("/projects/")
def projects():
    return render_template("projects.html")

@app.route("/experience/")
def experience():
    return render_template("experience.html")