#!/bin/python3

import os
import unittest


def minimum_swaps(arr):
    pass


class MinimumSwapTestCase(unittest.TestCase):
    pass


def main():
    unittest.main()


def run_hackerrank():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimum_swaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()


if __name__ == '__main__':
    if os.environ.get('OUTPUT_PATH', None) is None:
        main()
    else:
        run_hackerrank()