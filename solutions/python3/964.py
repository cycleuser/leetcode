
class Solution:
    def leastOpsExpressTarget(self, x: int, y: int) -> int:
        """
        计算最小操作次数来表示目标值y

        英文注释：Calculate the minimum number of operations to express target value y.
        """
        pos = neg = k = 0
        # 当y不为0时持续循环
        while y:
            y, cur = divmod(y, x)
            if k:  # 如果k大于0，处理正负值
                # 更新pos和neg的最小操作次数
                pos, neg = min(cur * k + pos, (cur + 1) * k + neg), min((x - cur) * k + pos, (x - cur - 1) * k + neg)
            else:  # 初始情况下处理正负值
                # 直接计算当前位置的正负操作次数
                pos, neg = cur * 2, (x - cur) * 2
            k += 1  # 每次循环k加一，表示当前层级

        # 返回最小的操作次数减1
        return min(pos, k + neg) - 1
