
def get_med_idx(n: int, lb: int) -> int:
    return (n - 1) // 2 + lb


def median(arr1: list[int], lb1: int, arr2: list[int], lb2: int, n: int) -> int:
    """Find the median of 2 sorted arrays"""

    # If each of the array is only size 1
    if n == 1:
        return min(arr1[lb1], arr2[lb2])
    
    # For each of the array
    median1 = get_med_idx(n, lb1)
    median2 = get_med_idx(n, lb2)

    if n % 2:
        # If arr1 median is smaller
        if (arr1[median1] < arr2[median2]):
            return median(arr1, median1, arr2, lb2, n//2 + 1)

        # If arr2 median is smaller
        return median(arr1, lb1, arr2, median2, n//2 + 1)

    # Even
    # If arr1 median is smaller
    if (arr1[median1] < arr2[median2]):
        return median(arr1, median1 + 1, arr2, lb2, n//2)

    # If arr2 median is smaller
    return median(arr1, lb1, arr2, median2 + 1, n//2)


if __name__ == '__main__':

    print("# Test Cases #")
    cases = [
        # a1 , a2, n, ans #
        ([1], [2], 1, 1),
        ([41, 42], [43, 44], 2, 42),
        ([2, 3, 6], [1, 4, 5], 3, 3),
        ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5, 5),
        ([4, 5, 6, 10, 11, 12, 13], [1, 2, 3, 7, 8, 9, 14], 7, 7),
    ]

    failed = []
    for index, (arr1, arr2, n, ans) in enumerate(cases):
        result = median(arr1, 0, arr2, 0, n)
        if result != ans:
            failed.append(
                f"Case {index+1} failed. Expected {ans} but got {result}")
        else:
            print(f"Case {index+1} passed")
    if not failed:
        print("All cases passed")
    else:
        for fail in failed:
            print(fail)
