class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :param obstacleGrid: List[List[int]], grid with obstacles (1) and free cells (0)
        :return: int, number of unique paths from top-left to bottom-right
        """
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
            
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        
        # Initialize first cell
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        
        # Initialize first row
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]
                
        # Initialize first column
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
        
        # Fill dp table
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]