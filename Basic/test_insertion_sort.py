from InsertionSort import insertion_sort


def test_insertion_sort_random():
    array = [7, 3, 5, 1, 9, 4, 2, 6, 8]
    arr_cpy = array.copy()
    expected = sorted(array)
    insertion_sort(arr_cpy)
    assert arr_cpy == expected


def test_insertion_sort_reversed():
    array = [i for i in range(10, 0, -1)]
    arr_cpy = array.copy()
    expected = sorted(array)
    insertion_sort(arr_cpy)
    assert arr_cpy == expected


def test_insertion_sort_sorted():
    array = [i for i in range(10)]
    arr_cpy = array.copy()
    expected = sorted(array)
    insertion_sort(arr_cpy)
    assert arr_cpy == expected
