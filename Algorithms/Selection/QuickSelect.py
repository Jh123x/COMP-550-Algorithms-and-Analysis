from random import randint
import time


## Exerpt from merge sort ###################
from typing import List


def merge_sort(array: List[int], start: int, end: int) -> None:
    """Merge sort algorithm"""
    if start < end:
        mid = (start + end) // 2
        merge_sort(array, start, mid)
        merge_sort(array, mid + 1, end)
        merge(array, start, mid, end)
    return array


def merge(array: List[int], start: int, mid: int, end: int) -> None:
    """Merging subroutine"""
    left = array[start:mid + 1]
    right = array[mid + 1:end + 1]
    left.append(float("inf"))
    right.append(float("inf"))
    i = j = 0
    for k in range(start, end + 1):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1

#############################################


def get_median(arr: list[int]) -> int:
    """Get the median of a list"""
    if len(arr) == 1:
        return arr[0]

    sorted_arr = sorted(arr)
    size = len(arr)

    if size % 2 == 0:
        return sorted_arr[size // 2 - 1]

    return sorted_arr[size // 2]


def get_pivot(arr: list, lower: int, higher: int) -> int:
    """Getting a good pivot"""
    acc = []
    for i in range(lower, higher + 1, 5):
        end = min(higher + 1, i + 5)

        # Check that the each partition is < 5
        assert end - i <= 5, (i, end, higher, lower)

        a = arr[i:end]
        if len(a) == 0:
            continue
        acc.append(a)

    medians = []
    for grp in acc:
        me = get_median(grp)
        medians.append(me)

    if len(medians) > 5:
        return get_pivot(medians, 0, len(medians) - 1)

    return get_median(medians)


def swap(arr: list[int], index1: int, index2: int) -> None:
    assert index1 < len(arr) and index2 < len(arr), (index1, index2, len(arr))
    arr[index1], arr[index2] = arr[index2], arr[index1]


def quick_select(arr: list, lower: int, higher: int, target: int) -> int:
    """O(n) Order selection algorithm"""

    # Base Case
    if lower == higher == target - 1:
        return arr[lower]

    if higher - lower + 1 <= 5:
        return sorted(arr)[target - 1]

    median = get_pivot(arr, lower, higher)

    # Partition
    left_index = lower + 1
    right_index = higher

    while(left_index <= right_index):
        curr = arr[left_index]
        if curr <= median and (arr[lower] == median or curr < median):
            left_index += 1
        elif curr > median:
            swap(arr, left_index, right_index)
            right_index -= 1
        else:
            swap(arr, lower, left_index)

    swap(arr, lower, right_index)

    # Recursion
    if target == right_index + 1:
        return median

    if target < right_index:
        return quick_select(arr, lower, right_index - 1, target)

    return quick_select(arr, right_index + 1, higher, target)


if __name__ == '__main__':
    for size in range(1, 500):
        arr = [randint(0, 100) for _ in range(size)]

        total_sort_time = 0
        total_select_time = 0
        for target in range(size):

            array = arr.copy()

            # Sort time
            sort_start = time.time()
            sorted_arr = merge_sort(array, 0, len(arr) - 1)
            total_sort_time += time.time() - sort_start

            # Select Time
            start_time = time.time()
            select_target = quick_select(arr, 0, size - 1, target)
            total_select_time += time.time() - start_time

            assert select_target == sorted_arr[target -
                                               1], "Failed at {}".format(target)

        print(
            f"Size: {size}, Sort Time: {total_sort_time / size}, Avg Select Time: {total_select_time / size}")
