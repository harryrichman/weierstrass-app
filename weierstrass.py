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
    W = Counter()
    for v in G.nodes():
        red_K = reduce_canonical(G, v)
        W[v] = red_K[v] - g + 1
    return W

def run_random_cubic_ex():
    H = nx.random_regular_graph(3, 82)
    G = subdivide(H, 1)
    W = weierstrass_locus(G)

    pos_H = nx.kamada_kawai_layout(H, dim=3)
    pos = nx.spring_layout(
        G, pos=pos_H, fixed=pos_H.keys(), 
        k=0.005, dim=3
    )

    node_color = []
    for v in G.nodes():
        if W[v] > 0: node_color.append("tab:red")
        else: node_color.append("gray")
    create_3d_plot(G, pos, W, node_color)

if __name__ == "__main__":
    H = nx.frucht_graph()
    pos_H = nx.spring_layout(H, seed=52, scale=10)

    H2 = subdivide(H, 2)
    pos_H2 = nx.spring_layout(
        H2, pos=pos_H, fixed=pos_H.keys(),
        k=0.05, iterations=90
    )

    G = subdivide(H2, 7)
    pos = nx.spring_layout(
        G, pos=pos_H2, fixed=pos_H2.keys(),
        k=0.05, iterations=900
    )
    W = weierstrass_locus(G)

    colors = []
    for v in G.nodes():
        if W[v] > 0: colors.append("tab:red")
        else: colors.append("tab:gray")
    nx.draw(G, pos, node_color=colors, alpha=0.5)
    plt.show()