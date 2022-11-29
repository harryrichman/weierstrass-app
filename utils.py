import networkx as nx
import matplotlib.pyplot as plt

def subdivide(G, n):
    """
    returns graph obtained from subdividing each edge of G into n edges
    """
    # G = networkx graph
    # n = positive integer
    if (n < 1):
        raise ValueError("number of subdivisions must be positive integer")
    if (n == 1): return G
    Gsub = nx.create_empty_copy(G)
    for e in G.edges():
        (i, j) = e
        pair = str(i) + '-' + str(j) + '-'
        # add first and last edges in path
        Gsub.add_edge(i, pair + '1')
        Gsub.add_edge(pair + str(n-1), j)
        # add middle edges in path
        for k in range(1,n-1):
            Gsub.add_edge(pair + str(k), pair + str(k+1))
    return Gsub

if __name__ == "__main__":
    G = subdivide(nx.house_graph(), 40)
    pos = nx.spring_layout(G)
    nx.draw(G, pos)
    plt.show()