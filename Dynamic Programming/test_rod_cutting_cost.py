from RodCuttingCost import rod_cutting_cost


def test_trivial_case():
    prices = [10, 1, 2, 3]
    _, dp = rod_cutting_cost(prices, len(prices), 1)
    assert dp == [0, 10, 19, 28, 37]


def test_case_1():
    prices = [2, 1, 10]
    _, dp = rod_cutting_cost(prices, len(prices), 1)
    assert dp == [0, 2, 3, 10]

def test_case_2():
    prices = [1,1,4,1]
    _, dp = rod_cutting_cost(prices, len(prices), 1)
    assert dp == [0,1,1,4,4]

def test_case_3():
    prices = [100, 1]
    _, dp = rod_cutting_cost(prices, len(prices), 1)
    assert dp == [0, 100, 199]

def test_case_4():
    prices = [4, 1, 8, 3]
    _, dp = rod_cutting_cost(prices, len(prices), 1)
    assert dp == [0, 4, 7, 10, 13]

