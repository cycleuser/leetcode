
class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 获取网格的大小
        n = len(grid)
        
        # 计算顶视图面积，即非零元素的数量
        top = sum(grid[i][j] != 0 for i in range(n) for j in range(n))
        
        # 计算前视图面积，即每行的最大值之和
        front = sum(max(grid[i]) for i in range(n))
        
        # 计算侧视图面积，即每列的最大值之和
        side = sum(max(grid[i][j] for i in range(n)) for j in range(n))
        
        # 返回顶视图、前视图和侧视图面积的总和
        return top + front + side
