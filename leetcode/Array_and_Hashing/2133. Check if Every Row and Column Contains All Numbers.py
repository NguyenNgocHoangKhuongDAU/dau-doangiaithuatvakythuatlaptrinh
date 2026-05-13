class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)

        for row in matrix:
            if len(set(row)) != n:
                return False

        for col in range(n):
            s = set()

            for row in range(n):
                s.add(matrix[row][col])

            if len(s) != n:
                return False

        return True
        