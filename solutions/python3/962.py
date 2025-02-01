    
class Solution:
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        
        解题思路：
        1. 首先通过字典存储每个数值对应的所有索引位置，方便后续查找。
        2. 对原始列表A进行排序，以确定最左边和最右边的边界。
        3. 遍历排序后的A，计算当前数字对应的最大宽度。
        4. 更新最小索引值ind，确保最终结果正确。
        """
        ind, mx, index = float("inf"), 0, collections.defaultdict(list)
        
        # 构建字典index，键为数值，值为该数值对应的索引列表
        for i, num in enumerate(A):
            index[num].append(i)
            
        # 对原始数组进行排序
        A.sort()
        
        # 遍历排序后的A，计算最大宽度
        for i in range(len(A)):
            mx = max(mx, index[A[i]][-1] - ind)
            ind = min(ind, index[A[i]][0])
        
        return mx
    