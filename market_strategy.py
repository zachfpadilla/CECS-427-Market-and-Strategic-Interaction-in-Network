import networkx as nx
from cli import get_parser
from analysis import *
from visualization import visualize_graph
from verification import verify_bipartite_graph
parser = get_parser()
args = parser.parse_args()

G = None

try:
    G = nx.read_gml(args.graph_file)
    print(f"Successfully loaded graph from '{args.graph_file}'.")
    print(f"Nodes: {G.number_of_nodes()}, Edges: {G.number_of_edges()}")
except FileNotFoundError:
    print(f"Error: The file '{args.graph_file}' was not found.")
    exit(1)
except Exception as e:
    print(f"Error: Failed to parse GML file. Reason: {e}")
    exit(1)

if not verify_bipartite_graph(G):
    exit(1)

try:
    A, B = nx.bipartite.sets(G)

    print("Set A Prices")
    for node in A:
        node_label = G.nodes[node].get('label', node)
        price = G.nodes[node].get('price', 'N/A')
        print(f"{node_label}: {price}")
    
    print("Valuations")
    for node_a, node_b, attr in G.edges(A, data=True):
        valuation = attr.get('valuation', 'N/A')
        node_a_label = G.nodes[node_a].get('label', node_a)
        node_b_label = G.nodes[node_b].get('label', node_b)
        print(f"Node {node_b_label} valuation of node {node_a_label}: {valuation}")
except Exception as e:
        print(f"Error processing graph: {e}")
        exit(1)

if args.plot:
    print("\nGenerating plot...")
    visualize_graph(G)

