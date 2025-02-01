
class Solution:
    # 初始化解决方案类

    def minTotalDistance(self, grid):
        m, n = len(grid), len(grid[0])  # 获取网格的行数m和列数n
        
        # 提取所有有1的位置的x坐标和y坐标分别排序
        x = sorted(i for i in range(m) for j in range(n) if grid[i][j])
        y = sorted(j for i in range(m) for j in range(n) if grid[i][j])

        # 计算中位数作为平均位置
        avg_x = len(x) % 2 and x[len(x) // 2] or (x[len(x) // 2 - 1] + x[len(x) // 2]) / 2
        avg_y = len(y) % 2 and y[len(y) // 2] or (y[len(y) // 2 - 1] + y[len(y) // 2]) / 2

        # 计算所有点到平均位置的曼哈顿距离之和
        return int(sum(abs(avg_x - i) + abs(avg_y - j) for i, j in zip(x, y)))
