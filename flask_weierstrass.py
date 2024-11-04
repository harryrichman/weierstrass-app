from flask import (
    Flask,
    render_template,
    request,
)
import json
from networkx import Graph

from reduce import reduce_canonical

app = Flask(__name__)

@app.route("/")
def hello_world():
    # return "<p>Hello, world!</p>"
    return render_template("index.html")

@app.route("/get-red-divisor", methods=["POST"])
def get_red_divisor():
    app_data = request.form
    base_v = json.loads(app_data["base_v"])
    G = Graph(app_data["graph"])
    
    red_divisor = reduce_canonical(G, base_v)
    return json.dumps(red_divisor)
    pass