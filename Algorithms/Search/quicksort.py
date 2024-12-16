#!/bin/python3

import random
import unittest


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quicksort(arr, low, high):
    if low < high:
        # instead of deterministically choosing the pivot, random pivoting
        # selects a pivot randomly from the current subarray.
        # this random selection reduces the chance of consistently picking 
        # bad pivots (e.g., smallest or largest elements)
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

        pivot = partition(arr, low, high)

        # recursively sort the partitions
        quicksort(arr, low, pivot - 1)
        quicksort(arr, pivot + 1, high)
    
    return arr


class MinimumSwapTestCase(unittest.TestCase):
    def test_quicksort(self):
        arr = [7, 1, 3, 2, 4, 5, 6]
        expected_output = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(quicksort(arr, 0, len(arr) - 1), expected_output)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
