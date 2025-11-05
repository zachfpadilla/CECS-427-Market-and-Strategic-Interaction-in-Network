def update_prices(G, sellers_to_update, increment=1):
    """
    Increments the price for each seller in the given set.
    """
    for seller in sellers_to_update:
        if 'price' in G.nodes[seller]:
            G.nodes[seller]['price'] += increment
        else:
            G.nodes[seller]['price'] = increment
    return G