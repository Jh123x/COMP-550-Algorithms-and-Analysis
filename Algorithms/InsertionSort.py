

def insertion_sort(array: list) -> None:
    """Insertion sort"""

    # Iterate through the array
    for i in range(1, len(array)):
        curr = array[i]
        for j in range(0, i):
            if array[j] > curr:
                array[j], curr = curr, array[j]
        array[i] = curr


if __name__ == '__main__':
    array = [4, 3, 2, 1, 2, 3, 4, 5, 6]
    insertion_sort(array)
    print(array)
