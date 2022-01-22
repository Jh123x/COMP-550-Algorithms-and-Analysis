

def find_max_crossing_subarray(arr: list, low: int, mid: int, high: int) -> tuple[int, int, int]:
    """Find the maximum sum of a subarray crossing the midpoint"""
    left_sum = -float('inf')
    right_sum = -float('inf')

    sum = 0
    for i in range(mid, low - 1, -1):
        sum = sum + arr[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    sum = 0
    for i in range(mid + 1, high + 1):
        sum = sum + arr[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i

    return (max_left, max_right, left_sum + right_sum)


def find_max_subarray(arr: list, low: int, high: int) -> tuple:
    """Find the maximum sum of a subarray"""
    if low >= high:
        return (low, high, arr[low])

    mid = (low + high) // 2
    left = find_max_subarray(arr, low, mid)
    right = find_max_subarray(arr, mid + 1, high)
    cross = find_max_crossing_subarray(arr, low, mid, high)

    return max(left, right, cross, key=lambda x: x[2])

if __name__ == '__main__':
    arr = [1, -2, 3, -4, 5, -6, 7, -8, 9, - 10]
    result = find_max_subarray(arr, 0, len(arr) - 1)
    print(result)
    
