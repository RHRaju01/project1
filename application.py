from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/more", methods=["POST"])
def more():
    name = request.form.get("name")
    if name == "raju":
        return "You are a good boy Raju!"
    else:
        return render_template("more.html", name=name)

