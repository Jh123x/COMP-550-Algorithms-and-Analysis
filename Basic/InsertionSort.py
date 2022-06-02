def insertion_sort(array: list) -> None:
    """Insertion sort in place"""

    # Iterate through the array
    for i in range(1, len(array)):
        curr = array[i]
        for j in range(i):
            if array[j] > curr:
                array[j], curr = curr, array[j]  # Swap
        array[i] = curr
