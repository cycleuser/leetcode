
from itertools import product as pr


class Solution(object):
    """
    Class to find solutions based on a given function and target value.
    """

    def findSolution(self, customfunction, z):
        """
        Find all pairs (i, j) where 1 <= i, j <= z such that customfunction.f(i, j) == z.

        :param customfunction: A callable object representing the custom function
        :param z: Target value to match with the function's output
        :return: List of [i, j] pairs satisfying the condition
        """
        return [
            [i, j]
            for i, j in pr(range(1, z + 1), repeat=2)
            if customfunction.f(i, j) == z
        ]
