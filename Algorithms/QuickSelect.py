from random import randint

def get_median(arr: list[int]) -> int:
    """Get the median of a list"""
    assert len(arr) > 0 and len(arr) <= 5, arr

    if len(arr) == 1:
        return arr[0]

    sorted_arr = sorted(arr)
    size = len(arr)

    if size % 2 == 0:
        return sorted_arr[size // 2 - 1]

    return sorted_arr[size // 2]

def get_pivot(arr:list, lower:int, higher:int) -> int:
    """Getting a good pivot"""
    acc = []
    for i in range(lower, higher + 1, 5):
        end = min(higher + 1, i + 5)
        a = arr[i:end]
        if len(a) == 0:
            continue
        acc.append(a)

    medians = []
    for grp in acc:
        me = get_median(grp)
        medians.append(me)

    return get_median(medians)

def swap(arr:list[int], index1:int, index2:int) -> None:
    assert index1 < len(arr) and index2 < len(arr), (index1, index2, len(arr))
    arr[index1], arr[index2] = arr[index2], arr[index1]

def quick_select(arr: list, lower:int, higher:int, target:int) -> int:
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
    size = 9
    arr = [randint(0, 100) for _ in range(size)]
    for target in range(size):
        assert quick_select(arr, 0, size - 1, target) == sorted(arr)[target-1], "Failed at {}".format(target)
    
    