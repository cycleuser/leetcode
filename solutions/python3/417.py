
class Solution:
    def pacificAtlantic(self, matrix):
        """
        Pacific Atlantic Water Flow Problem
        
        :param matrix: List[List[int]], a matrix representing elevation heights
        :return: List[List[int]], positions that can flow to both the Pacific and Atlantic oceans
        """

        if not matrix or not matrix[0]:
            return []

        pac, atl, m, n = set(), set(), len(matrix), len(matrix[0])
        
        """
        Explore function for dfs.
        It adds current position to visited set if it can flow from current cell.
        :param i: row index
        :param j: column index
        :param ocean: the set of cells that can flow into this ocean
        """
        def explore(i, j, ocean):
            ocean.add((i, j))
            # Check top and left neighbors for Pacific Ocean exploration
            if i > 0 and (i - 1, j) not in ocean and matrix[i - 1][j] >= matrix[i][j]:
                explore(i - 1, j, ocean)
            # Check bottom neighbor for Atlantic Ocean exploration
            if i + 1 < m and (i + 1, j) not in ocean and matrix[i + 1][j] >= matrix[i][j]:
                explore(i + 1, j, ocean)
            # Check left neighbor for Pacific Ocean exploration
            if j > 0 and (i, j - 1) not in ocean and matrix[i][j - 1] >= matrix[i][j]:
                explore(i, j - 1, ocean)
            # Check right neighbor for Atlantic Ocean exploration
            if j + 1 < n and (i, j + 1) not in ocean and matrix[i][j + 1] >= matrix[i][j]:
                explore(i, j + 1, ocean)

        # Explore boundaries to identify cells that can flow into Pacific or Atlantic
        for i in range(m):
            if (i, 0) not in pac: 
                explore(i, 0, pac)
            if (m - 1, i) not in atl: 
                explore(m - 1, i, atl)

        for j in range(n):
            if (0, j) not in pac:
                explore(0, j, pac)
            if (i, n - 1) not in atl:
                explore(i, n - 1, atl)

        # Return cells that can flow into both oceans
        return [[x, y] for x, y in pac & atl]
