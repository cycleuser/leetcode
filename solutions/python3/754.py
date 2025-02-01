
class Solution:
    # 定义一个类，用于解决达到目标位置的问题

    def reachNumber(self, target):
        # 初始化当前位置、步数和目标值（取绝对值）
        pos, step, target = 0, 0, abs(target)
        
        # 当当前位置小于目标值或者当前位置与目标值的差为奇数时，继续移动
        while pos < target or (pos - target) % 2:
            step += 1          # 增加步数
            pos += step        # 移动到新位置
        
        return step           # 返回所需的最小步数
