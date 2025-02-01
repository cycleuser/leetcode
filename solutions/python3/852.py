
class Solution:
    # 寻找山脉数组中的峰值索引

    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]  # 输入的整数列表A
        :rtype: int         # 返回峰值元素的索引
        
        思路：找到最大值对应的索引即为峰值索引
        """
        mx = max(A)  # 找到列表中的最大值
        return A.index(mx)  # 返回最大值在列表中的索引
