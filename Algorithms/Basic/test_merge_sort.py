from MergeSort import merge_sort


def test_merge_sort_random():
    array = [7, 3, 5, 1, 9, 4, 2, 6, 8]
    arr_cpy = array.copy()
    expected = sorted(array)
    result = merge_sort(arr_cpy, 0, len(arr_cpy) - 1)
    assert result == expected


def test_merge_sort_reversed():
    array = [i for i in range(10, 0, -1)]
    arr_cpy = array.copy()
    expected = sorted(array)
    result = merge_sort(arr_cpy, 0, len(arr_cpy) - 1)
    assert result == expected


def test_merge_sort_sorted():
    array = [i for i in range(10)]
    arr_cpy = array.copy()
    expected = sorted(array)
    result = merge_sort(arr_cpy, 0, len(arr_cpy) - 1)
    assert result == expected
