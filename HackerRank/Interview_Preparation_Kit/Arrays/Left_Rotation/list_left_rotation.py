#!/bin/python3

import os
import unittest


def rotate_left(arr, shifts):
    return arr[shifts:] + arr[:shifts]


class ListLeftRotationTestCase(unittest.TestCase):
    def test_sample_test_case(self):
        # test 4 shifts and len(arr) == 5
        shifts = 4
        arr = [1, 2, 3, 4, 5]
        expected_output = [5, 1, 2, 3, 4]

        self.assertEqual(rotate_left(arr, shifts), expected_output)

        # test 2 shifts and len(arr) == 7
        shifts = 2
        arr = [1, 2, 3, 4, 5, 6, 7]
        expected_output = [3, 4, 5, 6, 7, 1, 2]

        self.assertEqual(rotate_left(arr, shifts), expected_output)


def main():
    unittest.main()


def run_hackerrank():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    _ = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = rotate_left(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


if __name__ == '__main__':
    if os.environ.get('OUTPUT_PATH', None):
        run_hackerrank()
    else:
        main()