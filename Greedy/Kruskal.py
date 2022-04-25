def get_top_parent(ufds: dict, edge1: str) -> str:
    if edge1 not in ufds:
        return edge1

    curr = ufds[edge1]
    while curr in ufds:
        curr = ufds[curr]

    # Compression
    ufds[edge1] = curr

    return curr


def add_as_parent(ufds: dict, child: str, parent: str) -> None:
    ufds[child] = parent


def kruskals(graph: dict[str, dict[str, int]]) -> list:
    # Create the UFDS
    edge_list = []

    # Convert AL to Edge list
    for key, value in graph.items():
        for key2, value2 in value.items():
            edge_list.append((value2, key, key2))

    # Sort the edgelist
    edge_list.sort(reverse=True)
    ufds = {}
    mst = []

    # Start the kruskal algorithm
    while len(edge_list):
        value, from_edge, to_edge = edge_list.pop()
        from_parent = get_top_parent(ufds, from_edge)
        to_parent = get_top_parent(ufds, to_edge)

        if from_parent == to_parent:
            continue

        mst.append((from_edge, to_edge, value))
        add_as_parent(ufds, from_parent, to_parent)
    return mst


if __name__ == '__main__':
    graph = {
        'A': {'B': 5, 'D': 5, 'E': 7},
        'B': {'A': 5, 'C': 4, 'D': 8, 'E': 2},
        'C': {'B': 4, 'D': 8, 'F': 4},
        'D': {'A': 5, 'B': 8, 'C': 8, 'F': 9, 'E': 3},
        'E': {'A': 7, 'B': 2, 'D': 3, 'F': 2},
        'F': {'C': 4, 'D': 9, 'E': 2}
    }
    result = kruskals(graph)
    print(result)
