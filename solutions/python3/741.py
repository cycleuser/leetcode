
class Solution(object):
    # 定义一个解决方案类

    def cherryPickup(self, grid):
        # 检查右下角是否为-1，如果是则返回0
        if grid[-1][-1] == -1:
            return 0
        
        memo, n = {}, len(grid)
        # 使用字典memo存储已经计算过的结果以避免重复计算

        def dp(i1, j1, i2, j2):
            # 检查状态是否已在memo中，如果是则直接返回
            if (i1, j1, i2, j2) in memo:
                return memo[(i1, j1, i2, j2)]

            # 判断当前坐标是否越界或遇到-1
            if n in (i1, j1, i2, j2) or -1 in (grid[i1][j1], grid[i2][j2]):
                return -1

            # 如果两个机器人同时到达最后一个位置，直接返回其樱桃数量
            if i1 == i2 == j1 == j2 == n - 1:
                return grid[-1][-1]

            # 计算四种移动方式的最大值
            mx = max(dp(i1+1, j1, i2+1, j2), dp(i1+1, j1, i2, j2+1),
                     dp(i1, j1+1, i2+1, j2), dp(i1, j1+1, i2, j2+1))

            # 处理越界或遇到-1的情况
            if mx == -1:
                out = -1
            elif i1 == i2 and j1 == j2:  # 如果两个机器人在同一位置
                out = mx + grid[i1][j1]
            else:
                out = mx + grid[i1][j1] + grid[i2][j2]

            # 将结果存入memo以备后续使用
            memo[(i1, j1, i2, j2)] = out

            return out
        
        # 从起始点开始递归搜索最大樱桃数量
        return max(0, dp(0, 0, 0, 0))
