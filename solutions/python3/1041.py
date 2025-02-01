
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """
        判断机器人在给定指令后是否会回到原点。
        
        :param instructions: 字符串，包含'G','L','R'三种指令
                            'G': 前进一格
                            'L': 左转90度
                            'R': 右转90度
        :return: 如果机器人在执行完所有指令后回到原点返回True, 否则返回False
        
        机器人的初始方向是北，使用(dx, dy)表示当前方向。
        为了简化代码逻辑，在四个周期内重复执行给定的指令集。
        最终检查机器人的位置是否回到了(0, 0)，且方向与初始一致。
        """
        x, y, dx, dy = 0, 0, 0, 1
        
        # 循环四次，确保模拟完整周期
        for _ in range(4):
            for ins in instructions:
                if ins == 'G':
                    # 前进一格
                    x += dx
                    y += dy
                elif ins == 'L':
                    # 左转90度
                    dx, dy = -dy, dx
                else:
                    # 右转90度
                    dx, dy = dy, -dx
        
        return x == 0 and y == 0
