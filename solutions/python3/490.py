
class Solution:
    def hasPath(self, maze, start, destination):
        """
        判断从起始位置能否到达目标位置。

        参数：
            maze: List[List[int]] - 代表迷宫的地图，1表示墙，0表示可通行。
            start: List[int] - 起始位置坐标 [x, y]。
            destination: List[int] - 目标位置坐标 [x, y]。

        返回值：
            bool - 如果能从起始位置到达目标位置则返回True，否则返回False。
        """
        m, n, stopped = len(maze), len(maze[0]), set()  # 获取迷宫的行数、列数以及已访问的位置集合

        def dfs(x, y):
            """
            深度优先搜索辅助函数。

            参数：
                x: int - 当前探索位置的x坐标。
                y: int - 当前探索位置的y坐标。

            返回值：
                bool - 如果从当前位置能到达目标位置则返回True，否则返回False。
            """
            if (x, y) in stopped:  # 检查当前位置是否已被访问过
                return False
            stopped.add((x, y))  # 标记当前位置已访问

            if [x, y] == destination:  # 判断是否到达目标位置
                return True

            for i, j in (-1, 0), (1, 0), (0, -1), (0, 1):
                newX, newY = x, y  # 初始化新的探索坐标
                while 0 <= newX + i < m and 0 <= newY + j < n and maze[newX + i][newY + j] != 1:
                    newX += i  # 沿着当前方向继续移动
                    newY += j

                if dfs(newX, newY):  # 如果从新位置能到达目标位置则返回True
                    return True
            return False

        return dfs(*start)  # 调用深度优先搜索函数，传入起始坐标
