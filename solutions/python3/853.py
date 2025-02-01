
class Solution:
    # 定义解决方案类

    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        """
        计算达到目标位置的车队数量
        
        :param target: 目标位置
        :param position: 每辆车的起始位置列表
        :param speed: 每辆车的速度列表
        :return: 达到目标位置的车队数量
        """
        
        res, s = 0, {pos: vel for pos, vel in zip(position, speed)}
        # 初始化结果计数器 res 和速度字典 s
        
        position.sort()
        # 对起始位置进行排序

        while position:
            cur = position.pop()
            res += 1
            # 弹出当前车的位置，并将车队数量加一
            
            while position and (s[position[-1]] - s[cur]) * (target - cur) / s[cur] >= cur - position[-1]:
                position.pop()
                # 如果后一辆车赶上前面的车，则弹出路劲位置列表
        
        return res
