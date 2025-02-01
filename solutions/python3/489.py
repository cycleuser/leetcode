
class Solution:
    def cleanRoom(self, robot, move=[(-1, 0), (0, -1), (1, 0), (0, 1)]):
        """
        清洁机器人清洁房间的算法实现。
        
        :param robot: 机器人对象，具有clean(), move(), turnLeft()方法
        :param move: 移动方向列表，默认为上下左右
        """

        def dfs(i, j, cleaned, ind):
            """
            深度优先搜索函数用于清洁房间。

            :param i: 当前横坐标
            :param j: 当前纵坐标
            :param cleaned: 已清理单元集合
            :param ind: 移动方向索引
            """

            robot.clean()  # 清洁当前格子
            cleaned.add((i, j))  # 标记为已清理

            k = 0
            for x, y in move[ind:] + move[:ind]:  # 遍历所有可能的方向
                if (i + x, j + y) not in cleaned and robot.move():  # 检查下一步是否可以移动且未被清理过
                    dfs(i + x, j + y, cleaned, (ind + k) % 4)  # 递归深度优先搜索

                    # 返回上一步，先右转两次，再左转一次
                    robot.turnLeft()
                    robot.turnLeft()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()

                robot.turnLeft()  # 尝试下一个方向之前总是先左转，确保每次尝试移动前都在原地
                k += 1

        dfs(0, 0, set(), 0)  # 从 (0, 0) 开始搜索
