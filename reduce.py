"""
Implement Dhar's burning algorithm for finding reduced representative 
in divisor class
"""

import networkx as nx

def canonical_div(G):
    # returns canonical divisor of G, as a dictionary
    # G = networkx graph
    K = {}
    for v in G.nodes():
        K[v] = G.degree[v] - 2
    return K

def reduce_canonical(G, q):
    # returns reduced representative of K(G) at q
    # G = networkx graph, q = vertex of G
    red_K = canonical_div(G)
    # check that q is a vertex of G
    if not (q in G.nodes()):
        raise ValueError("node " + str(q) + " not in graph")
    # repeat process: set fire at q, fire chips towards fire
    while True:
        (burned, noFire, frontier) = set_fire(G, red_K, q)
        # check whether whole graph is on fire
        if not burned:
            # print("before div:", red_K)
            chip_firing(G, red_K, noFire, frontier)
            # print("after div:", red_K)
        else: break
    return red_K

def chip_firing(G, red_K, noFire, frontier):
    # WARNING: modifies red_K in place
    # print("  fire chips on ", NoFire.nodes())
    # print("  with frontier", frontier)
    for v in frontier:
        for w in G.adj[v]:
            if not (w in noFire.nodes()):
                red_K[w] += 1
                red_K[v] -= 1
    return

def set_fire(G, D, q):
    """
    returns (bool, NoFire, frontier) where
      bool = whether fire spread to whole graph
      NoFire = subgraph of G which is not on fire
      frontier = boundary of NoFire
    G = networkx graph, D = divisor on V(G), q = vertex of G
    """
    # initialize "fire" and "no fire" subgraphs
    Fire = nx.Graph()
    NoFire = G.copy()
    # set q on fire, spread to q-edges
    Fire.add_node(q)
    Fire.add_edges_from(G.edges(q))
    NoFire.remove_node(q)
    # initialize "frontier" = boundary between fire and no-fire
    frontier = list(G.adj[q])
    # spread fire to undefended vertices
    while True:
        # print("frontier: ", frontier)
        fire_defended = True
        next_frontier = frontier.copy()
        for v in frontier:
            # compute number of incoming fires
            fire_count = Fire.degree[v]
            if fire_count > D[v]:
                # set neighbors on fire
                fire_defended = False
                next_frontier.remove(v)
                # print("testing vertex ", v)
                # print("add nodes to frontier: ", list(NoFire.adj[v]))
                for w in NoFire.adj[v]:
                    if not (w in next_frontier): next_frontier.append(w)
                # next_frontier = [*next_frontier, *(NoFire.adj[v])]
                NoFire.remove_node(v)
                Fire.add_edges_from(G.edges(v))
        # print("next frontier: ", next_frontier)
        frontier = next_frontier
        if len(frontier) == 0: 
            # print("empty frontier")
            return (True, Fire, [])
        if fire_defended:
            # print("fire defended")
            # apply chip firing move towards fire
            return (False, NoFire, frontier)

def q_effective_rep(G, D, q):
    # G = networkx graph, D = divisor on V(G), q = vertex of G
    # returns representative in [D] effective away from q
    pass
