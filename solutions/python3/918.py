
class Solution:
    # 定义一个类，用于解决带环的子数组最大和问题

    def maxSubarraySumCircular(self, A):
        # 初始化最小左侧和、最大右侧和、结果值、当前左侧和、当前右侧和以及前缀和
        lMn, rMx, res, lSm, rSm, preSm = float("inf"), [-float("inf")] * (len(A) + 1), -float("inf"), 0, 0, 0
        
        # 计算从右向左的前缀和，并更新最大右侧和
        for i in range(len(A) - 1, -1, -1):
            rSm += A[i]
            rMx[i] = max(rMx[i + 1], rSm)
        
        # 遍历数组，计算当前左侧和、最小左侧和，并更新结果值
        for i in range(len(A)):
            preSm += A[i]
            lMn = min(lMn, lSm)
            res = max(res, preSm, preSm - lMn, preSm + rMx[i + 1])
            lSm += A[i]
        
        return res
