
class Solution:
    # 定义一个辅助函数，计算累积和数组
    def cumSum(self, it):
        """
        :param it: 可迭代对象，包含索引与数值对
        :return: 累积和数组
        """
        sm = mn = 0
        sums = [0] * len(arr)
        for i, num in it:
            sm += num
            sums[i] = sm - mn
            mn = min(mn, sm)
        return sums
    
    # 计算最大子序列和
    def maximumSum(self, arr: List[int]) -> int:
        """
        :param arr: 输入整数数组
        :return: 最大非连续子序列和
        
        思路：通过计算前缀最小累积和与后缀最小累积和，找到最大非连续子序列和。
              前缀最小累积和用于处理正数的情况，后缀最小累积和用于处理负数情况。
        """
        
        # 计算左半部分的累积和数组
        lSum = self.cumSum(enumerate(arr))
        
        # 计算右半部分的累积和数组（逆序计算）
        rSum = self.cumSum(reversed(list(enumerate(arr))))
        
        res = -float('inf')
        for i, num in enumerate(arr):
            if num >= 0:
                cur = lSum[i] + rSum[-i-1] - num
            else:
                cur = lSum[i] + rSum[-i-1] - 2 * num
            
            res = max(res, cur)
        
        # 如果数组中有非负数，则返回最大子序列和，否则返回数组中的最大值
        return res if any(c >= 0 for c in arr) else max(arr)
