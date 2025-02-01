
class Solution:
    # 类用于解决最小路径和问题

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        prev = None  # 初始化前一层的节点值
        for tri in triangle:  # 遍历三角形中的每一层
            if prev:
                for i, num in enumerate(tri):  # 遍历当前层的每个数字
                    if i >= len(prev):
                        # 当前数字在上一层之后，只能从上一层左侧节点累加
                        tri[i] += prev[i - 1]
                    elif i == 0:
                        # 当前数字为当前层第一个元素，则只可累加上一层首个元素值
                        tri[i] += prev[0]
                    else:
                        # 取当前数字与上一层左侧和右侧最小值累加
                        tri[i] += min(prev[i - 1], prev[i])
            prev = tri  # 更新前一层为当前层

        return min(triangle[-1])  # 返回最后一层中的最小值，即为路径和的最小值
