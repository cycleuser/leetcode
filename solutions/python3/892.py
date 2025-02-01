
class Solution:
    # 定义一个求解表面积的方法
    def surfaceArea(self, grid):
        n, sm = len(grid), 0
        
        # 遍历每个格子
        for i in range(n):
            for j in range(n):
                # 计算当前格子的贡献值：高度 * 4（上下面） + 2（侧面）
                sm += grid[i][j] and (grid[i][j] * 4 + 2)
                
                # 检查上方
                if i > 0: 
                    sm -= min(grid[i - 1][j], grid[i][j])
                    
                # 检查左方
                if j > 0:
                    sm -= min(grid[i][j - 1], grid[i][j])
                
                # 检查下方
                if i < n - 1:
                    sm -= min(grid[i + 1][j], grid[i][j])
                    
                # 检查右方
                if j < n - 1: 
                    sm -= min(grid[i][j + 1], grid[i][j])
        
        return sm
