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


if __name__ == "__main__":
    array = [5, 3, 1, 2, 4]
    merge_sort(array, 0, len(array) - 1)
    print(array)
