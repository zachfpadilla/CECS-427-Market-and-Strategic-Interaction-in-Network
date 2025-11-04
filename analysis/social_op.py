import networkx as nx

TOLERANCE = 1e-7

def social_optimum(G, N, s, t, max_iter=100):
    """
    Computes the flow distribution for the Social Optimum.

    This is achieved by using the marginal cost function for pathfinding:
    MC_e(x_e) = d/dx[x_e * C_e(x_e)] = 2*a_e*x_e + b_e

    Uses the Frank-Wolfe algorithm.
    """

    #start with an all-or-nothing assignment
    flow = {e: 0.0 for e in G.edges()}
    try:
        path = nx.shortest_path(G, source=s, target=t, weight='b')
        for u, v in zip(path[:-1], path[1:]):
            edge = (u, v)
            if edge in flow:
                flow[edge] = float(N)
            else:
                print(f"Error: Path found edge ({u},{v}) not in DiGraph.")
                exit(1)

    except nx.NetworkXNoPath:
        print(f"Error: No path from {s} to {t} for initial flow.")
        return flow  #return zero flow

    for _ in range(max_iter):
        #compute current marginal costs based on flow
        current_costs = {}
        for u, v, data in G.edges(data=True):
            x_e = flow[(u, v)]
            a_e = float(data['a'])
            b_e = float(data['b'])

            #use marginal cost: mc(x) = 2*a*x + b
            cost = 2.0 * a_e * x_e + b_e

            #ensure cost is non-negative for shortest path algorithm
            current_costs[(u, v)] = max(0.0, cost)

        nx.set_edge_attributes(G, current_costs, 'current_cost')

        #find shortest path p* based on current marginal costs
        try:
            path_star = nx.shortest_path(G, source=s, target=t, weight='current_cost')
        except nx.NetworkXNoPath:
            break

        #create auxiliary flow y* (all-or-nothing on P*)
        y_flow = {e: 0.0 for e in G.edges()}
        for u, v in zip(path_star[:-1], path_star[1:]):
            y_flow[(u, v)] = float(N)

        #find optimal step size alpha (line search)
        direction = {e: y_flow[e] - flow[e] for e in G.edges()}

        numerator = 0.0
        denominator = 0.0

        for u, v, data in G.edges(data=True):
            d_e = direction[(u, v)]
            if abs(d_e) < TOLERANCE:
                continue

            x_e = flow[(u, v)]
            a_e = float(data['a'])
            b_e = float(data['b'])

            #use marginal cost function for line search
            cost_e = 2.0 * a_e * x_e + b_e
            numerator += cost_e * d_e
            denominator += 2.0 * a_e * (d_e ** 2)

        if denominator < TOLERANCE:
            alpha = 1.0 if numerator < 0 else 0.0
        else:
            alpha = -numerator / denominator

        alpha = max(0.0, min(1.0, alpha))  # Clip alpha to [0, 1]

        #update flow
        max_change = 0.0
        for e in flow:
            new_x_e = (1.0 - alpha) * flow[e] + alpha * y_flow[e]
            change = abs(new_x_e - flow[e])
            if change > max_change:
                max_change = change
            flow[e] = new_x_e

        #check convergence
        if max_change < TOLERANCE:
            break

    return flow