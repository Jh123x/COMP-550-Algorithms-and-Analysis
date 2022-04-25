from Prims import prims


def test_prims_single_vertex():
    graph = {
        "a": {}
    }
    assert prims(graph) == []

def test_prims_single_edge():
    graph = {
        "a": {"b": 1}
    }
    assert prims(graph) == [("a", "b", 1)]

def test_prims_trivial():
    graph = {
        "a": {"b": 1, "c": 2},
        "b": {"a": 3, "c": 4},
        "c": {"a": 6, "b": 5}
    }
    assert prims(graph) == [("a", "b", 1), ("a", "c", 2)]

def test_prims_random():
    graph = {
        'A': {'B': 5, 'D': 5, 'E': 7},
        'B': {'A': 5, 'C': 4, 'D': 8, 'E': 2},
        'C': {'B': 4, 'D': 8, 'F': 4},
        'D': {'A': 5, 'B': 8, 'C': 8, 'F': 9, 'E': 3},
        'E': {'A': 7, 'B': 2, 'D': 3, 'F': 2},
        'F': {'C': 4, 'D': 9, 'E': 2}
    }
    result = prims(graph)
    assert set(result) == set((("B", "E", 2), ('E', 'F', 2),
                      ('E', 'D', 3), ('B', 'C', 4), ("A", "B", 5)))
