"""
This is a recreated implementation of Destination Cities challenge
as in HackSussex Coder's Cup 2024 by Layton Burchell.
Link: https://www.youtube.com/live/VixYfv0UEyE?si=ATP8LrPdFv8HECiP&t=738

Recreated by: Luis Esteban Rodriguez <rodriguezjluis0@gmail.com>
GH: @metalerk
"""

from typing import List
from destination_city_test_cases import runTests


def Solution(paths: List[List[str]]) -> str:
    outs = set()
    ins = set()

    for a, b in paths:
        outs.insert(a)
        ins.insert(b)

    return [b for b in ins if b not in outs][0]

# testing
runTests(Solution)
