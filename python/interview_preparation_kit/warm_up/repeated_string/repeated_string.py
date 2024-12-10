#!/bin/python3
"""
Repeated String Problem Solution
--------------------------------

This script provides a solution to the "Repeated String" problem, which calculates 
how many times a specified character ('a') appears in the first n characters of 
an infinitely repeating string.

Author: Luis Esteban Rodriguez
Email: rodriguezjluis0@gmail.com
Github: https://github.com/metalerk
"""

import os
import unittest

from collections import Counter


def check_string_lenght(s: str) -> bool:
    """
    Ensures string lenght meets constraints.

    Parameters:
    s (str): Text String.

    Return:
    bool: True if constraints are met. Otherwise, False.
    """
    return True if len(s) > 0 and len(s) <= 100 else False


def check_number_of_chars(n: int) -> bool:
    """
    Ensures number of characters meets constraints.

    Parameters:
    n (int): Number of characters.

    Returns:
    bool: True if constraints are met. Otherwise, False.
    """
    return True if n > 0 and n <= 10**12 else False


def count_repetitions(s: str, n: int, math: bool = False) -> int:
    """
    Counts number of repeated a's.

    Parameters:
    s (str): Text String.
    n (int): Number of characters.
    math (bool): Flag for mathematical calculation or generator count.

    Returns:
    int: Number os a's in s string.
    """
    if math:
        str_len = len(s)
        number_of_as = count_repetitions(s, 1)
        ratio = n // str_len
        remaining_letters = n % str_len

        total = (number_of_as * ratio) + count_repetitions(s[:remaining_letters], 1)
        return total
    else:
        # Benchmarking with large numbers using list and generator
        # showed no significant difference between both. However, for
        # large number is a good practice to use generators since they
        # retrieve itens on demand.
        return Counter((c for c in s if c.lower() == "a"))["a"]


def repeatedString(s: str, n: int) -> int:
    """
    Orchestrates the calculation.

    Parameters:
    s (str): Text String.
    n (int): Number of characters.

    Returns:
    int: Number os a's in s string.
    """
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
        if s.lower() == "a":
            return n
        return 0

    return count_repetitions(s, n, math=True)


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

    def test_very_large_number(self):
        s = "kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm"
        n = 736778906400
        self.assertEqual(repeatedString(s, n), 51574523448)

    def test_unmatched_constraints(self):
        """Test unmatched constraints"""
        s = "abc" * 34
        n = 2
        with self.assertRaises(ValueError):
            repeatedString(s, n)

        s = "abc"
        n = (10**12) + 1
        with self.assertRaises(ValueError):
            repeatedString(s, n)


def main():
    """Main function."""
    unittest.main()


def run_hackerrank():
    """Uses hackerrank execution parameters."""
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
