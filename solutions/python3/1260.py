
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # 将二维列表展平为一维列表
        chain = [r for row in grid for r in row]
        
        # 计算实际需要右移的步数，避免不必要的大循环
        k %= len(chain)
        
        # 右移操作：将链表分为两部分，后k个元素移动到前面
        chain = chain[-k:] + chain[:-k]
        
        # 将一维列表重新组织为二维列表
        return [chain[i : i + len(grid[0])] for i in range(0, len(chain), len(grid[0]))]
