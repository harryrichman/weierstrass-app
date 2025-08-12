import random

from reduce import *
from weierstrass import *
from utils import *
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def tent_graph():
    G = nx.Graph()
    G.add_nodes_from(['a','b','c','ab','ac1','ac2',
                      'bc1','bc2'])
    G.add_edges_from([('a','ab'), ('ab','b'),
                      ('a','ac1'), ('ac1','c'),
                      ('a','ac2'), ('ac2','c'),
                      ('b','bc1'), ('bc1','c'),
                      ('b','bc2'), ('bc2','c')])
    return G

def loop_of_loops():
    G = nx.Graph()
    G.add_edges_from(
        [(0,1), (1,2), (2,3), (3,4), (4,5), 
         (5,10), (10,11), (11,12), (12,13), (13,0),
         (0,6), (6,1), (2,7), (7,3), (4,8), (8,5)]
    )
    return G

def frucht_graph(var=0):
    """
    returns one of the five asymmetric cubic graphs on 12 vertices
    """
    if var == 0:
        return nx.frucht_graph()
    else:
        if var == 1:
            adjacency_dict = {
                1: [2, 8, 0],
                2: [3, 0],
                3: [4, 11],
                4: [5, 10],
                5: [6, 7],
                6: [7, 9],
                7: [8],
                8: [9],
                9: [10],
                10: [11],
                11: [0]
            }
            ## debug
            # adjacency_dict = {1: [5, 2], 2: [5, 6]}
        elif var == 2:
            adjacency_dict = {
                1: [2, 5, 0],
                2: [3, 6],
                3: [4, 9],
                4: [5, 7],
                5: [6],
                6: [7],
                7: [8],
                8: [9, 11],
                9: [10],
                10: [11, 0],
                11: [0]
            }
        elif var == 3:
            adjacency_dict = {
                1: [2, 7, 0],
                2: [3, 11],
                3: [4, 9],
                4: [5, 10],
                5: [6, 0],
                6: [7, 8],
                7: [8],
                8: [9],
                9: [10],
                10: [11],
                11: [0]
            }
        elif var == 4:
            adjacency_dict = {
                1: [2, 7, 0],
                2: [3, 6],
                3: [4, 9],
                4: [5, 11],
                5: [6, 8],
                6: [7],
                7: [8],
                8: [9],
                9: [10],
                10: [11, 0],
                11: [0]
            }
        else:
            raise ValueError
        return nx.Graph(adjacency_dict)

def whitney_flip_pair(var=0):
    """
    constructs a pair of cubic graphs which differ by a Whitney flip.
    both graphs have genus 9
    """
    adjacency_dict = {
        1: [2, 4],
        2: [3, 5],
        3: [4, 5],
        4: [6],
        5: [7],
        6: [7, 8],
        7: [8],
        9: [10, 12],
        10: [11, 13],
        11: [12, 13],
        12: [14],
        13: [15],
        14: [15, 16],
        15: [16]
    }
    G = nx.Graph(adjacency_dict)
    if var == 0:
        G.add_edges_from([(1, 16), (8, 9)])
    elif var == 1:
        G.add_edges_from([(1, 9), (8, 16)])
    else:
        raise ValueError
    return G

def run_whitney_flip_ex():
    plt.subplot(1, 2, 1)
    G = whitney_flip_pair(var=0)
    W = weierstrass_locus(G)
    # pos = nx.kamada_kawai_layout(G, dim=2)
    pos = nx.spring_layout(G, iterations=500)
    node_color = []
    for v in G.nodes():
        if W[v] > 0: node_color.append((1,0.2,0.2,0.8))
        else: node_color.append((0.8,0.8,0.8,0.8))
    nx.draw(G, pos, labels=W, node_color=node_color)

    plt.subplot(1, 2, 2)
    G = whitney_flip_pair(var=1)
    W = weierstrass_locus(G)
    # pos = nx.kamada_kawai_layout(G, dim=2)
    pos = nx.spring_layout(G, iterations=500)
    node_color = []
    for v in G.nodes():
        if W[v] > 0: node_color.append((1,0.2,0.2,0.8))
        else: node_color.append((0.8,0.8,0.8,0.8))
    nx.draw(G, pos, labels=W, node_color=node_color)

    plt.show()

def run_random_cubic_ex(g=22, seed=None):
    # set random seed
    if seed is not None:
        random.seed(seed)

    (G, W, pos, node_color) = random_cubic_graph(g=g)
    nx.draw(G, pos, labels=W, node_color=node_color)
    plt.show()
    # create_3d_plot(G, pos, W, node_color)

def random_cubic_graph(g=22):
    """
    Returns (G, W, pos, node_color) where
        G: random cubic graph of specified genus
        W: Weierstrass locus
        pos: position data
        node_color: node color data
    """
    H = nx.random_regular_graph(3, 2*g - 2)
    G = subdivide(H, 1)
    W = weierstrass_locus(G)

    pos_H = nx.kamada_kawai_layout(H, dim=2)
    pos = nx.spring_layout(
        G, pos=pos_H, fixed=pos_H.keys(), 
        k=0.005, dim=2
    )

    node_color = []
    for v in G.nodes():
        if W[v] > 0: node_color.append((1,0.2,0.2,0.8))
        else: node_color.append((0.8,0.8,0.8,0.8))
    return (G, W, pos, node_color)

def run_tent_example():
    G = tent_graph()
    # G = nx.frucht_graph()
    W = weierstrass_locus(G)

    print(W)

    node_color = []
    for v in G.nodes():
        if W[v] > 0: node_color.append("tab:red")
        else: node_color.append("gray")
    options = {
        "labels": W,
        "node_color": node_color
    }
    pos = nx.spring_layout(G, seed = 52)
    nx.draw(G, pos, **options)
    plt.show()

def run_loop_of_loops_example():
    H = loop_of_loops()
    G = subdivide(H, 12)
    W = weierstrass_locus(G)

    node_color = []
    for v in G.nodes():
        if W[v] > 0: node_color.append("tab:red")
        else: node_color.append("gray")
    options = {
        "labels": W,
        "node_color": node_color
    }
    pos = nx.kamada_kawai_layout(G)
    nx.draw(G, pos, **options)
    plt.show()

def run_frucht_example(var=0):
    G = frucht_graph(var=var)
    # G = nx.random_geometric_graph(20, 0.225, seed=89)

    # produce graph options
    def make_options(G, q):
        red_K = reduce_canonical(G, q)
        # set node color options
        node_color = []
        for v in red_K:
            if v == q: 
                node_color.append('tab:green')
            elif red_K[v] > 0:
                node_color.append('#1f78b4') # default node color
            else:
                node_color.append("gray")
        options = {
            "labels": red_K,
            "node_color": node_color
        }
        return options

    pos = nx.spring_layout(G, seed=52)

    for (i, q) in enumerate([2, 3, 9, 4, 1, 8, 11, 5, 7, 0, 6, 10]):
        # strange order of vertex indices q chosen based on var=0 graph
        plt.subplot(3, 4, i+1)
        options = make_options(G, q)
        nx.draw(G, pos, **options)

    plt.show()

def run_random_cubic_collage_ex(g=6, seed=None):
    # set random seed
    if seed is not None:
        random.seed(seed)

    for i in range(12):
        plt.subplot(3, 4, i+1)
        (G, W, pos, node_color) = random_cubic_graph(g=g)
        nx.draw(G, pos, labels=W, node_color=node_color)
    plt.show()

def run_frucht_3d(var=0):
    # H = nx.frucht_graph()
    H = frucht_graph(var=var)
    G = subdivide(H, 7)
    W = weierstrass_locus(G)
    node_color = []
    for v in G.nodes():
        if W[v] > 0: node_color.append("tab:red")
        else: node_color.append("gray")

    pos_H = nx.kamada_kawai_layout(H, dim=3)
    pos = nx.spring_layout(G, k=0.005, pos=pos_H, fixed=pos_H.keys(), dim=3)
    create_3d_plot(G, pos, W, node_color)

def run_prism_example():
    H = nx.Graph()
    edges = [(0,1), (1,2), (2,0), (3,4), (4,5), (5,3), (0,3), (1,4), (2,5)]
    H.add_edges_from(edges)
    G = subdivide(H, 10)
    W = weierstrass_locus(G)

    node_color = []
    for v in G.nodes():
        if W[v] > 0: node_color.append("tab:red")
        else: node_color.append("gray")
    pos = nx.kamada_kawai_layout(G, dim=3)
    create_3d_plot(G, pos, W, node_color)

def run_slant_example():
    H = nx.Graph()
    H.add_edges_from([(0,1), (0,2), (1,3), (2,3), (4,5), (4,6), (5,7), (6,7),
                      (0,8), (8,9), (9,4), (3,10), (10,11), (11,7), (8,11)])
    G = subdivide(H, 6)
    W = weierstrass_locus(G)

    node_color = []
    for v in G.nodes():
        if W[v] > 0: node_color.append("tab:red")
        else: node_color.append("gray")
    options = {
        "labels": W,
        "node_color": node_color
    }
    pos = nx.kamada_kawai_layout(G, dim=3)
    create_3d_plot(G, pos, W, node_color)

def create_3d_plot(G, pos, labels, node_color):
    # 3d spring layout
    # Extract node and edge positions from the layout
    node_xyz = np.array([pos[v] for v in G.nodes()])
    edge_xyz = np.array([(pos[u], pos[v]) for u, v in G.edges()])

    # Create the 3D figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Plot the nodes - alpha is scaled by "depth" automatically
    ax.scatter(*node_xyz.T, s=100, ec="w", c=node_color)

    # Plot the edges
    for vizedge in edge_xyz:
        ax.plot(*vizedge.T, color="tab:gray")

    # Plot node labels
    for xyz, v in zip(node_xyz, G.nodes()):
        if labels[v] > 0:
            label = '%d' % (labels[v])
            ax.text(xyz[0], xyz[1], xyz[2], label)

    def _format_axes(ax):
        """Visualization options for the 3D axes."""
        # Turn gridlines off
        ax.grid(False)
        # Suppress tick labels
        for dim in (ax.xaxis, ax.yaxis, ax.zaxis):
            dim.set_ticks([])
        # Set axes labels
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")

    _format_axes(ax)
    fig.tight_layout()
    plt.show()

def create_2d_plot(G, labels, node_color):
    # 2d spring layout
    pos = nx.kamada_kawai_layout(G, dim=2)
    # Extract node and edge positions from the layout
    node_xy = np.array([pos[v] for v in G.nodes()])
    edge_xy = np.array([(pos[u], pos[v]) for u, v in G.edges()])

    # Create the 2D figure
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Plot the nodes
    ax.scatter(*node_xy.T, s=100, ec="w", c=node_color)

    # Plot the edges
    for vizedge in edge_xy:
        ax.plot(*vizedge.T, color="tab:gray")

    # Plot node labels
    for xy, v in zip(node_xy, G.nodes()):
        if labels[v] > 0:
            label = '%d' % (labels[v])
            ax.text(xy[0], xy[1], label)

    def _format_axes(ax):
        """Visualization options for the 3D axes."""
        # Turn gridlines off
        ax.grid(False)
        # Suppress tick labels
        for dim in (ax.xaxis, ax.yaxis):
            dim.set_ticks([])
        # Set axes labels
        # ax.set_xlabel("x")
        # ax.set_ylabel("y")

    _format_axes(ax)
    fig.tight_layout()
    plt.show()

if __name__ ==  "__main__":
    # run_frucht_3d(var=0)
    # run_random_cubic_ex(g=8)
    # run_random_cubic_collage_ex(g=13, seed=42)
    # run_frucht_example(var=0)
    run_whitney_flip_ex()

    ## WARNING: bug in output of the following:
    # run_random_cubic_collage_ex(g=7, seed=120)
