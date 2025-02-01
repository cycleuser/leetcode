    
class Solution:
    def robotSim(self, commands: list[int], obstacles: list[tuple[int]]) -> int:
        """
        解决问题：给定一系列命令和障碍物列表，计算机器人在执行所有命令后可能达到的最大距离的平方。
        
        参数：
            - commands: 一个整数列表，表示机器人的移动指令。正数为前进步数，-2 表示左转，-1 表示右转。
            - obstacles: 一个二维整数列表，表示障碍物的位置。

        返回值：机器人执行所有命令后可能达到的最大距离的平方。
        """
        i, j, mx = 0, 0, 0
        # 方向定义：向下、左、向上、右；d 表示当前方向
        d, move = 3, [(-1, 0), (0, -1), (1, 0), (0, 1)]
        # 将障碍物列表转换为集合以提高查找效率
        obstacles = set(map(tuple, obstacles))
        
        for command in commands:
            if command == -2:  # 右转
                d = (d + 1) % 4
            elif command == -1:  # 左转
                d = (d - 1) % 4
            else:
                x, y = move[d]
                while command and (i + x, j + y) not in obstacles:
                    i += x
                    j += y
                    command -= 1
            mx = max(mx, i ** 2 + j ** 2)
        return mx
