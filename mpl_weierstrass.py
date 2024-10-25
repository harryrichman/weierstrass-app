"""
Displays a graph, where clicking on a vertex produces the reduced 
representative of the canonical divisor at that vertex.
"""

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np
from reduce import *
from weierstrass import *
from utils import *

class ReducibleGraphWidget:
    """
    Attributes:
        self.G = networkx graph
        self.W = Weierstrass locus of G
        self.pos = position coordinates
    """
    def __init__(self, G, pos):
        self.G = G
        self.pos = pos
        self.genus = G.number_of_edges() - G.number_of_nodes() + 1
        self.W = None

        self.ax = None
        self.press = None

    def connect(self):
        """connect to all events necessary"""
        self.cidpress = self.ax.figure.canvas.mpl_connect(
            'pick_event', self.on_pick
        )
        self.cidwbutton = self.w_button.on_clicked(self.on_w_press)
        self.cidrbutton = self.r_button.on_clicked(self.on_r_press)

    def draw(self):
        G, pos = self.G, self.pos
        fig, ax = plt.subplots()
        self.ax = ax
        ax.set_title('Click on vertex to reduce canonical divisor')

        # adjust the main plot to make room for the sliders
        fig.subplots_adjust(bottom=0.15)

        # Create a `matplotlib.widgets.Button` to reset
        ax_reset = fig.add_axes([0.6, 0.025, 0.3, 0.04])
        self.r_button = Button(
            ax_reset, 'Reduced divisor (reset)', hovercolor='0.975')
        ax_weier = fig.add_axes([0.15, 0.025, 0.25, 0.04])

        self.w_button = Button(
            ax_weier, 'Weierstrass locus', hovercolor='0.975')
        
        # transpose array 'pos' using zip
        xs, ys = zip(*[pos[v] for v in G.nodes()])
        # plot points with picker event option
        self.points, = ax.plot(
            # 10 points tolerance
            xs, ys, 'o', picker=True, pickradius=10 
        )
        options = self.make_start_options()
        nx.draw_networkx_edges(G, pos, ax=self.ax)
        self.drawn_nodes = nx.draw_networkx_nodes(
            G, pos, ax=self.ax, node_color=options["node_color"])
        # drawn_labels is a dict whose values are ax.text() objects
        self.drawn_labels = nx.draw_networkx_labels(
            G, pos, ax=self.ax, labels=options["labels"])
    
    def make_start_options(self):
        colors = []
        for v in G.nodes():
            colors.append("tab:blue" if G.degree[v] > 2 else "gray")
        labels = {}
        for v in G.nodes():
            labels[v] = (
                "" if G.degree[v] == 2 else str(G.degree[v] - 2)
            )
        options = {
            "node_color": colors,
            "labels": labels
        }
        return options

    def make_reduce_options(self, q):
        G, g = self.G, self.genus
        red_K = reduce_canonical(G, q)
        # set node color options
        node_color = []
        for v in red_K:
            if v == q: 
                color = 'tab:red' if red_K[v] >= g else 'y'
                node_color.append(color)
            else:
                color = 'tab:blue' if red_K[v] > 0 else 'gray'
                node_color.append(color)
        positive_labels = {}
        for v in red_K:
            el = red_K[v]
            positive_labels[v] = el if el > 0 else ""
        options = {
            "labels": positive_labels,
            "node_color": node_color
        }
        return options

    def make_weierstrass_options(self):
        G, g, W = self.G, self.genus, self.W
        if W == None:
            print("W not stored, computing now")
            W = weierstrass_locus(G)
            self.W = W
        else: 
            print("W divisor stored")
        positive_labels = {}
        for v in G.nodes():
            el = (W[v] if W[v] > 0 else '')
            positive_labels[v] = el
        colors = []
        for v in G.nodes():
            color = 'tab:red' if W[v] > 0 else 'tab:gray'
            colors.append(color)
        options = {
            "labels": positive_labels,
            "node_color": colors
        }
        return options

    def on_pick(self, event):
        print("picked vertex", *event.ind)
        G = self.G
        if event.artist != self.points:
            return
        n = len(event.ind)
        if not n:
            return
        for dataind in event.ind:
            v = list(G.nodes())[dataind]
            options = self.make_reduce_options(v)
            # update node colors to show support of reduce divisor
            self.drawn_nodes.set_color(options["node_color"])
            # update labels to reflect reduced divisor coefficients
            for v in G.nodes():
                t = self.drawn_labels[v]
                label = options["labels"][v]
                t.set_text(label)
        self.ax.figure.canvas.draw()

    def on_w_press(self, event):
        options = self.make_weierstrass_options()
        # update node colors to show support of reduce divisor
        self.drawn_nodes.set_color(options["node_color"])
        # update labels to reflect reduced divisor coefficients
        for v in G.nodes():
            t = self.drawn_labels[v]
            label = options["labels"][v]
            t.set_text(label)
        self.ax.set_title('Weierstrass locus of canonical divisor')
        self.ax.figure.canvas.draw()

    def on_r_press(self, event):
        options = self.make_start_options()
        # update node colors to show support of reduce divisor
        self.drawn_nodes.set_color(options["node_color"])
        # update labels to reflect reduced divisor coefficients
        for v in G.nodes():
            t = self.drawn_labels[v]
            label = options["labels"][v]
            t.set_text(label)
        self.ax.set_title('Click on vertex to reduce canonical divisor')
        self.ax.figure.canvas.draw()

if __name__ ==  "__main__":

    # H = nx.frucht_graph()
    adj_mat = np.array([
        [0,1,1,0,0,0,0,0,0,0],
        [1,0,1,1,0,0,0,0,0,0],
        [1,1,0,0,1,0,0,0,0,0],
        [0,1,0,0,0,1,0,0,0,0],
        [0,0,1,0,0,1,1,0,0,0],
        [0,0,0,1,1,0,0,1,0,0],
        [0,0,0,0,1,0,0,0,1,0],
        [0,0,0,0,0,1,0,0,1,1],
        [0,0,0,0,0,0,1,1,0,1],
        [0,0,0,0,0,0,0,1,1,0]
    ])
    adj_mat = np.array(
        [[0,1,1,0,0,0,0,0,0,0,0,0,0],
         [1,0,1,1,0,0,0,0,0,0,0,0,0],
         [1,1,0,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,0,0,0,0,0,0,1,0,0],
         [0,0,1,0,0,0,0,0,0,0,0,1,1],
         [0,0,0,0,0,0,0,1,0,0,1,0,1],
         [0,0,0,0,0,0,0,0,1,0,0,1,0],
         [0,0,0,0,0,1,0,0,1,1,0,0,0],
         [0,0,0,0,0,0,1,1,0,1,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0],
         [0,0,0,1,0,1,0,0,0,0,0,0,0],
         [0,0,0,0,1,0,1,0,0,0,0,0,0],
         [0,0,0,0,1,1,0,0,0,0,0,0,0]]
    )
    adj_mat = np.array(
        [[0,1,1,0,0,0,0,0,0,0,0,0,0,0],
         [1,0,1,1,0,0,0,0,0,0,0,0,0,0],
         [1,1,0,0,1,0,0,0,0,0,0,0,0,0],
         [0,1,0,0,0,0,0,0,0,0,1,0,0,0],
         [0,0,1,0,0,0,0,0,0,0,0,1,1,0],
         [0,0,0,0,0,0,0,1,0,0,1,0,0,1],
         [0,0,0,0,0,0,0,0,1,0,0,1,0,0],
         [0,0,0,0,0,1,0,0,1,1,0,0,0,0],
         [0,0,0,0,0,0,1,1,0,1,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0,0],
         [0,0,0,1,0,1,0,0,0,0,0,0,0,0],
         [0,0,0,0,1,0,1,0,0,0,0,0,0,0],
         [0,0,0,0,1,0,0,0,0,0,0,0,0,1],
         [0,0,0,0,0,1,0,0,0,0,0,0,1,0]]
    )
    edge_list = [()]
    # H = nx.from_numpy_array(adj_mat)
    adj_dict = {
        0: (1, 2),
        1: (0, 2, 3),
        2: (0, 1, 4),
        3: (1,5, 12),
        4: (2,6),
        5: (3,7),
        6: (4,8),
        7: (5,9),
        8: (6,10, 13),
        9: (7,10, 11),
        10: (8,9, 11),
        11: (9, 10),
        12: (3, 13),
        13: (12, 8),
    }
    H = nx.Graph(adj_dict)
    pos_H = {
        0: (-1,1),
        1: (0,0),
        2: (0,2),
        3: (1,0),
        4: (1,2),
        5: (2,0),
        6: (2,2),
        7: (3,0),
        8: (3,2),
        9: (4,0),
        10: (4,2),
        11: (5,1),
        12: (1.7,0.7),
        13: (2.3,1.3),
    }
    # pos_H = nx.spring_layout(H, seed=52)
    G = subdivide(H, 40)
    # pos = nx.spring_layout(G, k=0.015, pos=pos_H, fixed=pos_H.keys())
    pos = nx.spring_layout(
        G, pos=pos_H, fixed=pos_H.keys(),
        k=0.018, 
        iterations=2000,
    )

    widget = ReducibleGraphWidget(G, pos)
    widget.draw()
    widget.connect()

    plt.show()