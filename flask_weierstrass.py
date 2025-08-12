from flask import (
    Flask,
    render_template,
    request,
)
import json
import networkx as nx

from reduce import reduce_canonical
from weierstrass import weierstrass_locus

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/get-reduced-div", methods=["POST"])
def get_red_divisor():
    app_data = request.form
    # debugging
    print("app_data: ", app_data)
    edge_list = json.loads(app_data["adj"])
    base_v = json.loads(app_data["base_v"])
    G = nx.Graph(edge_list)
    
    red_divisor = reduce_canonical(G, base_v)
    return json.dumps(red_divisor)
    
@app.route("/get-weierstrass-div", methods=["POST"])
def get_weierstrass_div():
    app_data = request.form

    w_divisor = weierstrass_locus(G)
    return json.dumps(w_divisor)
