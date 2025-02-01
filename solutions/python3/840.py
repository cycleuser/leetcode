
class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        计算给定网格中包含的魔方数。
        """
        res = 0
        
        # 遍历可能的3x3子网格
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                # 检查行、列和对角线的和是否相等
                if (sum(grid[i][j:j+3]) == 
                    sum(grid[i+1][j:j+3]) == 
                    sum(grid[i+2][j:j+3]) == 
                    sum(grid[k][j] for k in range(i, i + 3)) == 
                    sum(grid[k][j+1] for k in range(i, i + 3)) == 
                    sum(grid[k][j+2] for k in range(i, i + 3)) ==
                    (grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]) == 
                    (grid[i+2][j] + grid[i+1][j+1] + grid[i][j+2])):
                    
                    # 检查数字是否为1到9的唯一组合
                    if set(grid[i][j:j+3] + grid[i+1][j:j+3] + grid[i+2][j:j+3]) == {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                        res += 1
        
        return res
