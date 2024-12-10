#!/bin/python3

import os
import unittest

from collections import Counter


# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#


def check_string_lenght(s: str) -> bool:
    """ "Ensures string lenght meets constraints"""
    return True if len(s) > 0 and len(s) <= 100 else False


def check_number_of_chars(n: int) -> bool:
    """ "Ensures number of characters meets constraints"""
    return True if n > 0 and n <= 10**12 else False


def expand_string(s: str, n: int) -> str:
    """Expands the string"""
    if len(s) >= n:
        return s

    expanded_str = ""
    while True:
        for c in s:
            if len(expanded_str) >= n:
                return expanded_str
            expanded_str += c


def count_repetitions(s: str) -> int:
    """Counts number of repeated a's"""
    # Benchmarking with large numbers using list and generator
    # showed no significant difference between both. However, for
    # large number is a good practice to use generators since they
    # retrieve itens on demand.
    return Counter((c for c in s if c.lower() == "a"))["a"]


def repeatedString(s: str, n: int) -> int:
    """Does the whole thing"""
    # check types
    if not isinstance(s, str):
        raise ValueError(f"Invalid type {type(s)}: Must be str")
    if not isinstance(n, int):
        raise ValueError(f"Invalid type {type(n)}: Must be int")

    # check constraints
    if not check_string_lenght(s):
        raise ValueError("Invalid string s: Length must be 1 <= s <= 10")
    if not check_number_of_chars(n):
        raise ValueError("Invalid number n: Value must range between 1 <= n <= 10^12")

    # no explanation needed here, is it?
    if len(s) == 1:
        if s.lower() == 'a':
            return n
        return 0

    return count_repetitions(expand_string(s, n))


class RepeatedStringTestCase(unittest.TestCase):
    """Handles exercise test cases"""

    def test_repeated_string_correct(self):
        """Test correct and expected behaviour"""
        s = "aba"
        n = 10
        self.assertEqual(repeatedString(s, n), 7)

        s = "a"
        n = 1000000000000
        self.assertEqual(repeatedString(s, n), 1000000000000)

        s = "asdfg"
        n = 20
        self.assertEqual(repeatedString(s, n), 4)

        s = "sdfg"
        n = 3
        self.assertEqual(repeatedString(s, n), 0)

    def test_repeated_string_incorrect(self):
        """Test incorrect behaviour"""
        s = "abca"
        n = 3
        self.assertNotEqual(repeatedString(s, n), 8)

    def test_unmatched_constraints(self):
        """Test unmatched constraints"""
        s = "abc" * 34
        n = 2
        with self.assertRaises(ValueError) as ctx:
            repeatedString(s, n)

        s = "abc"
        n = (10**12) + 1
        with self.assertRaises(ValueError) as ctx:
            repeatedString(s, n)


def main():
    # unittest.main()
    s = "x"
    n = 970770
    print(repeatedString(s, n))


def run_hackerrank():
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + "\n")

    fptr.close()


if __name__ == "__main__":
    if os.environ.get("OUTPUT_PATH", None) is None:
        main()
    else:
        run_hackerrank()
