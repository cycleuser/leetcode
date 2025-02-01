
class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        # 初始化结果、起始位置和连续有效子数组长度计数器
        res, start, diff = 0, -1, 0
        
        for i in range(len(A)):
            if L <= A[i] <= R:
                # 当前元素在范围内，更新连续有效子数组长度并累加结果
                diff, res = i - start, res + i - start
            elif A[i] > R:
                # 当前元素超过范围，重置起始位置和连续有效子数组长度计数器
                diff, start = 0, i
            else:
                # 当前元素在范围内但还未达到最大值，累加当前的连续有效子数组长度
                res += diff
        
        return res
