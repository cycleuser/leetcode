    
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """
        :param moves: 包含字符 'R', 'L', 'U', 'D' 的字符串，分别代表右、左、上、下四个方向的移动
        :return: 如果最终回到原点，则返回 True；否则返回 False
        """
        x, y = 0, 0
        # 遍历每个字符，并更新坐标
        for char in moves:
            if char == "R": 
                x += 1
            elif char == "L": 
                x -= 1
            elif char == "U": 
                y += 1
            elif char == "D": 
                y -= 1
        
        # 检查是否回到原点
        return (x == 0 and y == 0)
    