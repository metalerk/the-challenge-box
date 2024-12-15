#!/bin/python3

import os
import unittest


def validate_array(arr):
    if not arr or (len(arr) != len(arr[0])):
        raise Exception("Invalid array: Must be an integer square matrix NxN.")


def hourglass_sum(arr):
    # validate array
    validate_array(arr)

    highest_sum = []

    for n in range(len(arr) - 2):
        for m in range(len(arr) - 2):
            a = arr[n][m]
            b = arr[n][m + 1]
            c = arr[n][m + 2]
            d = arr[n + 1][m + 1]
            e = arr[n + 2][m]
            f = arr[n + 2][m + 1]
            g = arr[n + 2][m + 2]

            highest_sum.append(a + b + c + d + e + f + g)

    return max(highest_sum)


class TwoDimensionArrayTestCase(unittest.TestCase):
    def test_hourglass_sum(self):
        arr = [
            [-9, -9, -9, 1, 1, 1],
            [0, -9, 0, 4, 3, 2],
            [-9, -9, -9, 1, 2, 3],
            [0, 0, 8, 6, 6, 0],
            [0, 0, 0, -2, 0, 0],
            [0, 0, 1, 2, 4, 0],
        ]
        self.assertEqual(hourglass_sum(arr), 28)
    
    # this was a failing test during the first submit
    def test_test_case_3_hackerrank(self):
        arr = [
            [-1, -1, 0, -9, -2, -2],
            [-2, -1, -6, -8, -2, -5],
            [-1, -1, -1, -2, -3, -4],
            [-1, -9, -2, -4, -4, -5],
            [-7, -3, -3, -2, -9, -9],
            [-1, -3, -1, -2, -4, -5],
        ]
        self.assertEqual(hourglass_sum(arr), -6)
    
    def test_invalid_array(self):
        arr = [
            [-1, -1, 0, -9, -2, -2],
            [-2, -1, -6, -8, -2, -5],
            [-1, -1, -1, -2, -3, -4],
            [-1, -9, -2, -4, -4, -5],
            [-7, -3, -3, -2, -9, -9],
        ]
        with self.assertRaises(Exception):
            hourglass_sum(arr)


def main():
    unittest.main()


def run_hackerrank():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglass_sum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


if __name__ == '__main__':
    if os.environ.get('OUTPUT_PATH', None) is None:
        main()
    else:
        run_hackerrank()
