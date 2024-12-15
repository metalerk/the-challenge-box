#!/bin/python3
import os
import unittest


# Complete the countingValleys function below.
def countingValleys(s):
    valleys = 0
    altitude = 0
    alledgedly_valley = 0
    for step in s:
        if step.lower() == "u":
            altitude += 1
        else:
            altitude -= 1
        if altitude <= -1:
            alledgedly_valley = 1
        if altitude == 0:
            if alledgedly_valley:
                alledgedly_valley = 0
                valleys += 1
    return valleys


class CountingValleysTestCase(unittest.TestCase):
    def test_correct_behaviour(self):
        self.assertEqual(countingValleys("UDDDUDUU"), 1)


def main():
    unittest.main()


def run_hackerrank():
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    _ = int(input())

    s = input()

    result = countingValleys(s)

    fptr.write(str(result) + "\n")

    fptr.close()


if __name__ == "__main__":
    if os.environ.get("OUTPUT_PATH", None) is None:
        main()
    else:
        run_hackerrank()
