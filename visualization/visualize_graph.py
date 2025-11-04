import networkx as nx
import matplotlib.pyplot as plt
from analysis import *

def visualize_graph(G):
    """Visualizes the graph based on computed metrics."""
    if G.number_of_nodes() == 0:
        print("Cannot plot an empty graph.")
        return

    print(f"Generating plot...")
    plt.figure(figsize=(12, 12))
    A, B = nx.bipartite.sets(G)
    pos = nx.bipartite_layout(G, A)

    node_colors = ["blue" if G.nodes[node]["bipartite"] == 0  else "red" for node in G.nodes()]
    edge_labels = nx.get_edge_attributes(G, "valuation")
    nx.draw(G, pos, with_labels=True, labels=nx.get_node_attributes(G, "price"), node_color=node_colors, font_color='white')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.7)

    plt.show()
