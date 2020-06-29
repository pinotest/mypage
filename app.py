from flask import render_template, request, redirect
from flask import Flask

app = Flask(__name__)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html")
    elif request.method == 'POST':
        print(request.form['sendEmail'])
        return redirect("/contact")


@app.route("/me")
def me():
    items = ["Imię: Stefan", "Nazwisko: Burczymucha"]
    return render_template("me.html", items=items)
