from flask import (
    Flask,
    render_template,
    request,
)
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    # return "<p>Hello, world!</p>"
    return render_template("index.html")

@app.route("/get-divisor", methods=["POST"])
def get_divisor():
    pass