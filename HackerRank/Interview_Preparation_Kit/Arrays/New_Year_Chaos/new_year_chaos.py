#!/bin/python3

import os
import io
import sys
import unittest

from test_values import VERY_LARGE_ARRAY_TEST_CASE


BASE_POSITION = lambda n: [x for x in range(n)]


def minimum_bribes(q):
    total_bribes = 0

    # this ensures the loop stops at 0
    for i in range(len(q) - 1, -1, -1):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return

        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                total_bribes += 1

    print(total_bribes)



class MinimumBribesTestCase(unittest.TestCase):
    def test_minimun_bribes_expected(self):

        test_cases = [
            # person 5 bribes person 4
            ([1, 2, 3, 5, 4, 6, 7, 8], "1"),
            # person 4 bribes 3 people
            ([4, 1, 2, 3, 5, 6, 7, 8], "Too chaotic"),
            # few bribes
            ([2, 1, 5, 3, 4], "3"),
            ([1, 2, 5, 3, 7, 8, 6, 4], "7"),
            # very large array
            VERY_LARGE_ARRAY_TEST_CASE,
        ]

        for tc in test_cases:
            # create new stdout
            captured_output = io.StringIO()
            
            # capturing stdout
            sys.stdout = captured_output
            
            # minimum_bribes print redirected
            minimum_bribes(tc[0])

            # flush stdout
            sys.stdout = sys.__stdout__.flush()

            # asserts
            self.assertEqual(captured_output.getvalue().strip(), tc[1])


def main():
    unittest.main()


def run_hackerrank():
    t = int(input().strip())

    for _ in range(t):
        _ = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimum_bribes(q)
    return None

if __name__ == '__main__':
    if os.environ.get('OUTPUT_PATH', None):
        run_hackerrank()
    else:
        main()
