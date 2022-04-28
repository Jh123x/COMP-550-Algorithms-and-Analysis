from RodCutting import rod_cutting


def test_trivial_case():
    prices = [1, 5, 10]
    _, dp = rod_cutting(prices, len(prices))
    assert dp == [0, 1, 5,10]

def test_one_step():
    prices = [1,7,1,1]
    _, dp = rod_cutting(prices, len(prices))
    assert dp == [0, 1, 7, 8, 14]

def test_size_1():
    prices = [100]
    _, dp = rod_cutting(prices, len(prices))
    assert dp == [0, 100]

def test_size_2():
    prices = [4, 1, 8, 3]
    _, dp = rod_cutting(prices, len(prices))
    assert dp == [0, 4, 8, 12, 16]