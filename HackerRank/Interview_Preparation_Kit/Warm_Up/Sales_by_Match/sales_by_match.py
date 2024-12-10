#!/bin/python3

import os
import unittest

from collections import Counter


def sockMerchant(ar):
    return sum([int(i / 2) for i in Counter(ar).values()])


# unit tests
class SockMerchantTestCase(unittest.TestCase):
    def test_sock_merchant(self):
        ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
        self.assertEqual(sockMerchant(ar), 3)
        

def main():
    unittest.main()


def run_hackerrank():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    _ = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

if __name__ == "__main__":
    if os.environ.get("OUTPUT_PATH", None) is None:
        main()
    else:
        run_hackerrank()
