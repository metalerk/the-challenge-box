"""
This is a recreated implementation of Destination Cities challenge
test as in HackSussex Coder's Cup 2024 by Layton Burchell.
Since test files are not shown, I've recreated my own version of it.
Link: https://www.youtube.com/live/VixYfv0UEyE?si=ATP8LrPdFv8HECiP&t=738

Recreated by: Luis Esteban Rodriguez <rodriguezjluis0@gmail.com>
GH: @metalerk
"""

import unittest


class DestinationCityTestCase(unittest.TestCase):
    def __init__(self, solution_func):
        super(self.__class__, self).__init__()
        self.solution_func = solution_func
    
    # docs say "In most uses of TestCase, you will neither change the methodName
    # nor reimplement the default runTest() method". Gotta check this out more in deep.
    # Fix taken from: https://stackoverflow.com/a/19087323
    # Relevant docs: https://docs.python.org/3/library/unittest.html#unittest.TestCase
    def runTest(self):
        pass

    def test_solution(self):
        test_input = [
            ["London", "Paris"],
            ["Paris", "Tokyo"],
            ["Tokyo", "New York"]
        ]
        expected_output = "New York"
        self.assertEquals(
            self.solution_func(test_input),
            expected_output
        )


def runTests(solution):
    suite = unittest.TestSuite()
    suite.addTest(DestinationCityTestCase(solution_func=solution))
    unittest.TextTestRunner(verbosity=3).run(suite)
