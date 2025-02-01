
from functools import lru_cache

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        """
        计算跳马从原点移动到给定位置所需的最小步数。
        
        Args:
            x (int): 目标位置的x坐标
            y (int): 目标位置的y坐标
        
        Returns:
            int: 跳马到达目标位置所需的最小步数
        """
        
        @lru_cache(None)
        def dfs(i, j):
            """
            深度优先搜索辅助函数，计算从(x, y)移动到(0, 0)的最短路径。

            Args:
                i (int): 当前x坐标
                j (int): 当前y坐标
            
            Returns:
                int: 到达(0, 0)所需的步数
            """
            if i == j == 0:
                # 如果已经到达原点，返回0步
                return 0
            if i == 1 and j == 0 or j == 1 and i == 0:
                # 如果距离为(1, 0)或(0, 1)，无法一步到达原点，返回无穷大表示不可达
                return float('inf')
            # 尝试两个可能的跳跃方向，并取最小步数
            return min(dfs(abs(i - 2), abs(j - 1)), dfs(abs(i - 1), abs(j - 2))) + 1
        
        # 考虑到负坐标，转换为绝对值开始搜索
        return dfs(abs(x), abs(y))
