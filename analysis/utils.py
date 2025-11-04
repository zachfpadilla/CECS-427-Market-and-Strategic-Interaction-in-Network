def edge_cost(n, a, b):
    accumulator = 0
    for i in range(1, int(n) + 1):
        accumulator += (a * i)
        accumulator += b
    return accumulator

def total_cost_path(G, n, path):
    cost = 0
    for u, v in zip(path[:-1], path[1:]):
        edge = G[u][v]
        cost += edge_cost(n, edge['a'], edge['b'])
    return cost
