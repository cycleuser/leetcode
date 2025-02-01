
class Solution:
    # 定义一个Solution类，包含minSteps方法用于计算最小操作步数

    def minSteps(self, n: int) -> int:
        # 初始化当前数量cur、复制的数量copy以及操作步骤steps
        cur, copy, steps = 1, 0, 0
        
        # 当当前数量不等于目标值n时，继续循环
        while cur != n:
            if copy < cur and (n - cur) % cur == 0:  # 判断是否可以执行粘贴操作
                copy = cur  # 将当前数量复制到剪贴板中
            else:
                cur += copy  # 执行复制+粘贴操作，增加当前数量
            
            steps += 1  # 每次循环后操作步数加一
        
        return steps  # 返回最小操作步数
