import heapq

graph = {
    'A': {'B': 5, 'D': 5, 'E': 7},
    'B': {'A': 5, 'C': 4, 'D': 8, 'E': 2},
    'C': {'B': 4, 'D': 8, 'F': 4},
    'D': {'A': 5, 'B': 8, 'C': 8, 'F': 9, 'E': 3},
    'E': {'A': 7, 'B': 2, 'D': 3, 'F': 2},
    'F': {'C': 4, 'D': 9, 'E': 2}
}

source = 'A'
arr = list(map(lambda x: (x[1],source,x[0]), graph['A'].items()))
heapq.heapify(arr)
visited = set('A')
edges = []

while len(visited) < len(graph):
    weight, from_edge, to_edge = heapq.heappop(arr)
    if to_edge in visited:
        continue
    visited.add(to_edge)
    edges.append((from_edge, to_edge, weight))
    for new_to_edge, weight in graph[to_edge].items():
        if new_to_edge in visited:
            continue
        new_add = (weight, to_edge, new_to_edge)
        heapq.heappush(arr, new_add)


print(edges)
