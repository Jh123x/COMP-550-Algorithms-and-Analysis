def dfs(adj_l: dict[str, dict[str, int]], source: str, sink: str):
    """Depth first search"""
    visited = set()
    stack = [source]
    path = []

    while stack:
        curr = stack.pop()

        if curr == sink:
            return path + [sink]

        if curr not in visited:
            visited.add(curr)
            for next_node, weight in adj_l[curr].items():
                if weight == 0:
                    continue
                if next_node not in visited:
                    stack.append(next_node)
                    path.append(curr)
                    break

    return []


def find_min_flow_on_path(adj_l, path):
    """Find min flow on path"""
    min_flow = float('inf')
    for i in range(len(path) - 1):
        curr = path[i]
        next = path[i + 1]
        min_flow = min(min_flow, adj_l[curr][next])
    assert min_flow > 0, f"{min_flow}\n{path}\n{adj_l}"
    return min_flow


def ford_fulkerson(adj_l: dict[str, dict[str, int]], source: str, sink: str) -> int:
    """Ford Fulkerson algorithm"""
    if source == sink:
        return float('inf')

    max_flow = 0
    residual_graph = {}

    # Deep copy of adj_l
    for node in adj_l:
        residual_graph[node] = {}
        for next_node, weight in adj_l[node].items():
            residual_graph[node][next_node] = weight

    while True:
        path = dfs(residual_graph, source, sink)
        if not path:
            break

        # Find min flow of path
        curr_flow = find_min_flow_on_path(residual_graph, path)

        assert curr_flow > 0

        # Add the min flow to the edges
        for i in range(len(path) - 1):
            curr = path[i]
            next = path[i+1]

            # Update to make it exists before adding
            if next not in residual_graph:
                residual_graph[next] = {}
            if next not in residual_graph[curr]:
                residual_graph[curr][next] = 0
            if curr not in residual_graph[next]:
                residual_graph[next][curr] = 0

            assert residual_graph[curr][next] - curr_flow >= 0

            residual_graph[curr][next] -= curr_flow
            residual_graph[next][curr] += curr_flow

        max_flow += curr_flow

    return max_flow


if __name__ == '__main__':
    graph1 = {
        "s": {"a": 10, "c": 10},
        "a": {"b": 4, "c": 2, "d": 8},
        "b": {"t": 10},
        "c": {"d": 9},
        "d": {"b": 6, "t": 10},
        "t": {}
    }

    graph2 = {
        "s": {'a': 100, "b": 100},
        "a": {'c': 7},
        "b": {"c": 3},
        "c": {"t": 1},
        "t": {}
    }

    graph3 = {
        "s": {"a": 3, "b": 2},
        "a": {"t": 2, "b": 5},
        "b": {"t": 3},
        "t": {}
    }

    graph4 = {
        "s": {"t": 20}
    }

    graphs = [
        graph1,
        graph2,
        graph3,
        graph4
    ]

    results = [
        19,
        1,
        5,
        20
    ]

    for graph, expected in zip(graphs, results):
        r = ford_fulkerson(graph, "s", "t")
        assert r == expected, f"Expected: {expected} - Got: {r}"
