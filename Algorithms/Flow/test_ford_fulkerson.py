from FordFulkerson import ford_fulkerson

def test_fordfulkerson_trivial_graph():
    graph = {
        "s": {"t": 10}
    }
    assert ford_fulkerson(graph, "s", "t") == 10

def test_fordfulkerson_no_flow():
    graph = {
        "s": {"a": 0},
        "t": {}
    }
    assert ford_fulkerson(graph, "s", "t") == 0

def test_fordfulkerson_inf_flow():
    graph = {
        "s": {}
    }
    assert ford_fulkerson(graph, "s", "s") == float('inf')

def test_fordfulkerson_random():
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