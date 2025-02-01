
class Solution:
    # 计算最少生命值函数，输入是一个二维数组dungeon表示迷宫的地图
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])  # 获取地图的行数m和列数n

        # 从右下角向左上角反向遍历
        for i in range(m - 1, -1, -1):  # 逐行倒序
            for j in range(n - 1, -1, -1):  # 逐列倒序
                if i == m - 1 and j == n - 1:  # 到达右下角的单元格
                    dungeon[i][j] = max(1, 1 - dungeon[i][j])  # 确保初始位置的生命值不为0或负数
                elif j == n - 1:  # 处于最右侧的一列，只能从上一个单元格向下移动
                    dungeon[i][j] = max(1, dungeon[i + 1][j] - dungeon[i][j])
                elif i == m - 1:  # 处于最下侧的一行，只能从左边的单元格向右移动
                    dungeon[i][j] = max(1, dungeon[i][j + 1] - dungeon[i][j])
                else:
                    # 普通情况：考虑上方和右方两个方向的最大值
                    dungeon[i][j] = max(1, min(dungeon[i + 1][j], dungeon[i][j + 1]) - dungeon[i][j])

        return dungeon[0][0]  # 返回左上角的最小生命值，即为整个地图所需的最少初始生命值
