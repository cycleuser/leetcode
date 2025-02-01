
class Solution:
    # 定义一个类用于解决最大观光组合问题

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        # 初始化前缀和及最大值为负无穷
        pre, mx = 0, -float('inf')
        
        # 遍历数组中的每个元素及其索引
        for j, a in enumerate(A):
            # 更新当前可以组成的最优观光组合分数
            mx = max(mx, pre + a - j)
            # 更新前缀和，使其尽可能大
            pre = max(pre, a + j)
        
        # 返回最终的最大分数
        return mx
