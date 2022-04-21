from QuickSelect import quick_select
from random import randint


def test_quick_select_trivial():
    arr = [1]
    assert quick_select(arr, 0, 0, 0) == 1


def test_quick_select_2_items():
    arr = [1, 2]
    assert quick_select(arr, 0, 1, 1) == 1


def test_quick_select_random():
    for size in range(1, 100):
        arr = [randint(0, 100) for _ in range(size)]
        for target in range(size):
            array = arr.copy()
            sorted_arr = sorted(array)
            select_target = quick_select(arr, 0, size - 1, target)
            assert select_target == sorted_arr[target -
                                               1], "Failed at {}".format(target)
