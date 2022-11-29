"""
Find the Weierstrass locus of a graph, with attached multiplicities
"""

from utils import *
from reduce import *
import networkx as nx
import matplotlib.pyplot as plt

def weierstrass_locus(G):
    """
    returns divisor which encodes multiplicities of Weierstrass points
    of canonical divisor of G
    """
    # compute genus g
    g = G.number_of_edges() - G.number_of_nodes() + 1
    W = {}
    for v in G.nodes():
        red_K = reduce_canonical(G, v)
        W[v] = red_K[v] - g + 1
    return W

if __name__ == "__main__":
    H = nx.waxman_graph()
    G = subdivide(H, 6)
    pos = nx.kamada_kawai_layout(G)
    W = weierstrass_locus(G)
    colors = []
    for v in G.nodes():
        if W[v] > 0: colors.append("tab:red")
        else: colors.append("tab:gray")
    nx.draw(G, pos, node_color=colors, labels=W)
    plt.show()