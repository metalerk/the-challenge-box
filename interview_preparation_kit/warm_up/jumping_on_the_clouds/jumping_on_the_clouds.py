#!/bin/python3
"""
Jumping on the Clouds Problem Solution
---------------------------------------

This script provides a solution to the "Jumping on the Clouds" problem, which determines 
the minimum number of jumps required to reach the last cloud, given an array where:
- 0 represents a safe cloud
- 1 represents a dangerous cloud

The player can jump either one or two clouds forward if the target cloud is safe.

Author: Luis Esteban Rodriguez
Email: rodriguezjluis0@gmail.com
Github: https://github.com/metalerk
"""

from typing import List

import os
import unittest

from random import randrange


def validate_array(c: List[int]) -> bool:
    """
    Validates cloud array constraints.
    Raises an exception when conditions are not met.

    Parameters:
    c (List[int]): List of clouds. (0 for safe and 1 for dangerous)

    Returns:
    None: None
    """
    for i in c:
        if not isinstance(i, int) or i > 1 or i < 0:
            raise ValueError(
                f"Invalid type({type(i)}): Make sure clouds are only 0 or 1 int values."
            )
    if len(c) < 2 or len(c) > 100:
        raise IndexError(
            f"Invalid c lenght: Make sure clouds array length is between 2 and 100."
        )
    if c[0] or c[-1]:
        raise ValueError(
            f"Invalid step: Make sure start and end clouds are safe (set to 0)."
        )


def jumping_on_clouds(c: List[int]) -> int:
    """Counts jumps on clouds.

    Parameters:
    c (list): List containing safe and dangerous clouds.

    Returns:
    int: Number of the least steps needed to win.
    """
    current_step = 0
    clouds = len(c)
    steps = 0

    validate_array(c)

    for _ in c:
        # first checks if a two clouds step is possible by making sure
        # the player lands in a safe cloud
        if (current_step + 2) <= (clouds - 1) and not c[current_step + 2]:
            steps += 1
            current_step += 2
        # in case two clouds step lands in a dangerous cloud, tries one
        # cloud step instead
        elif (current_step + 1) <= (clouds - 1) and not c[current_step + 1]:
            steps += 1
            current_step += 1
    return steps


# unit tests
class JumpingOnCloudsTestCase(unittest.TestCase):
    """Handles jumping_on_clouds test cases."""

    def test_valid_cloud_array(self):
        """Test correct values and expected behaviour."""
        c = [0, 1, 0, 0, 0, 1, 0]
        self.assertEqual(jumping_on_clouds(c), 3)

    def test_invalid_cloud_array(self):
        """Test incorrect values."""
        # invalid cloud arrays since they start and/or end
        # in dangerous clouds
        test_cases = [
            [1, 1, 0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 1, 1],
        ]

        for case in test_cases:
            with self.assertRaises(ValueError):
                jumping_on_clouds(case)

        c = [0, 2, 3, 4, 5, 0]

        with self.assertRaises(ValueError):
            jumping_on_clouds(c)

    def test_out_of_boundaries_cloud_array(self):
        """Test out of boundaries array."""
        c = [randrange(0, 1) for _ in range(101)]

        with self.assertRaises(IndexError):
            jumping_on_clouds(c)


def main():
    """Main function."""
    unittest.main()


def run_hackerrank():
    """Uses hackerrank execution parameters."""
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    _ = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumping_on_clouds(c)

    fptr.write(str(result) + "\n")

    fptr.close()


if __name__ == "__main__":
    if os.environ.get("OUTPUT_PATH", None) is None:
        main()
    else:
        run_hackerrank()
