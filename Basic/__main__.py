from random import randint
from time import time_ns
from MergeSort import merge_sort
from InsertionSort import insertion_sort

if __name__ == '__main__':
    size = 5000 #Adjust to test different values
    array = [randint(0, 100) for i in range(size)]
    print(f"Sorting array of size {size}")

    start = time_ns()
    sorted(array)
    python_sort_time = time_ns() - start
    
    start = time_ns()
    insertion_sort(array.copy())
    time_taken = time_ns() - start

    start = time_ns()
    merge_sort(array.copy(), 0, len(array) - 1)
    m_time_taken = time_ns() - start

    
    
    print(f"Time taken for insertion sort:      {time_taken}ns")
    print(f"Time taken for merge sort:          {m_time_taken}ns")
    print(f"Time take for python built in sort: {python_sort_time}ns")