import networkx as nx

def find_constricted_set(preferred_graph, buyers, sellers):
    """
    Finds a constricted set of buyers in the preferred seller graph.
    A constricted set S (a subset of buyers) exists if the number of sellers
    they prefer as a group is smaller than the number of buyers in the group.
    Returns: (constricted_buyers, neighbor_sellers) or (None, None) if no set is found.
    """
    # 1. Find a maximum matching
    matching = nx.bipartite.maximum_matching(preferred_graph, top_nodes=buyers)

    # If matching is perfect, all buyers are matched, no constricted set
    if len(matching) == len(buyers):
        return None, None

    # 2. Find unmatched buyers
    unmatched_buyers = buyers - set(matching.keys())

    # 3. From unmatched buyers, find all reachable nodes via alternating paths
    # This identifies the group of buyers causing the constriction.
    q = list(unmatched_buyers)
    visited = set(unmatched_buyers)

    head = 0
    while head < len(q):
        u = q[head]
        head += 1

        if u in buyers:  # If node is a buyer, look for forward edges
            for v in preferred_graph.neighbors(u):
                if v not in visited:
                    visited.add(v)
                    q.append(v)
        else:  # If node is a seller, look for a backward matching edge
            # The matching dict is {buyer: seller}, so we need to find the key for our seller value
            matched_buyer = [b for b, s in matching.items() if s == u]
            if matched_buyer and matched_buyer[0] not in visited:
                b = matched_buyer[0]
                visited.add(b)
                q.append(b)

    constricted_buyers = visited.intersection(buyers)
    neighbor_sellers = visited.intersection(sellers)

    return constricted_buyers, neighbor_sellers