from FindMedianOf2SortedArrays import median


def test_find_median_trivial():
    arr1 = [1]
    arr2 = [2]
    n = 1
    assert median(arr1, 0, arr2, 0, n) == 1

def test_find_median_single_node():
    arr1 = [1, 2]
    arr2 = [2, 3]
    n = len(arr1)
    assert median(arr1, 0, arr2, 0, n) == 2

def test_find_median_random():
    cases = [
        # a1 , a2, n, ans #
        ([1], [2], 1, 1),
        ([41, 42], [43, 44], 2, 42),
        ([2, 3, 6], [1, 4, 5], 3, 3),
        ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5, 5),
        ([4, 5, 6, 10, 11, 12, 13], [1, 2, 3, 7, 8, 9, 14], 7, 7),
    ]

    for index, (arr1, arr2, n, ans) in enumerate(cases):
        result = median(arr1, 0, arr2, 0, n)
        assert result == ans, f"Case {index+1} failed. Expected {ans} but got {result}"