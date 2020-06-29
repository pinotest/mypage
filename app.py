from flask import render_template, request, redirect
from flask import Flask

app = Flask(__name__)


@app.route('/contact', methods=['POST'])
def contact_mail():
    return render_template("contact.html")


@app.route('/contact', methods=['GET'])
def contact():
    return render_template("contact.html")


@app.route("/me")
def me():
    return render_template("me.html")
