import networkx as nx
import math

def get_preferred_seller_graph(G, sellers, buyers):
    """
    Creates a new graph containing only the "preferred" edges.
    An edge (s, b) is preferred if seller s offers buyer b the highest payoff.
    Payoff is calculated as valuation - price.
    """
    preferred_graph = nx.Graph()
    preferred_graph.add_nodes_from(G.nodes(data=True))

    for buyer in buyers:
        max_payoff = -math.inf
        best_sellers = []

        # Find the maximum possible payoff for the current buyer
        for seller in G.neighbors(buyer):
            price = G.nodes[seller].get('price', 0)
            valuation = G.edges[seller, buyer].get('valuation', 0)
            payoff = valuation - price
            if payoff > max_payoff:
                max_payoff = payoff

        # Find all sellers offering that maximum payoff
        for seller in G.neighbors(buyer):
            price = G.nodes[seller].get('price', 0)
            valuation = G.edges[seller, buyer].get('valuation', 0)
            payoff = valuation - price
            if payoff == max_payoff:
                best_sellers.append(seller)

        # Add edges from the buyer to all their best sellers
        for seller in best_sellers:
            preferred_graph.add_edge(buyer, seller)

    return preferred_graph