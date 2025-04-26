#!/bin/python3

from typing import List
from functools import reduce

import os


def connectingTowns(n: int, routes: List[int]) -> int:
    return reduce(lambda x, y: x * y, routes) % 1234567


def run_unittests() -> None:
    #  (number_of_cities, routes, expected_output)
    case_1 = (3, [1, 3], 3)
    case_2 = (4, [2, 2, 2], 8)

    testcases = (
        case_1,
        case_2,
    )

    for test_case in testcases:
        assert connectingTowns(n=test_case[0], routes=test_case[1]) == test_case[2]


def hackerrank_run() -> None:
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        routes = list(map(int, input().rstrip().split()))

        result = connectingTowns(n, routes)

        fptr.write(str(result) + "\n")

    fptr.close()


if __name__ == "__main__":
    if os.environ.get("OUTPUT_PATH", None) is not None:
        hackerrank_run()
    else:
        run_unittests()
