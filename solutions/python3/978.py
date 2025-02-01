
class Solution:
    # 定义一个类用于解决最大湍流子数组的问题

    def maxTurbulenceSize(self, A: list[int]) -> int:
        """
        计算数组A中的最大湍流子数组长度。
        :param A: 输入的整数列表
        :return: 最大的湍流子数组长度
        
        逻辑解析：
        - 首先通过比较相邻元素确定每个位置上两数是否成升序或降序关系，形成一个布尔数组
        - 然后遍历布尔数组，统计连续不同趋势的最长子序列长度
        """
        
        # 创建一个布尔列表来记录每对相邻元素的趋势（True表示升序，False表示降序）
        arr = [A[i-1] < A[i] for i in range(1, len(A))]
        
        # 初始化当前最大湍流子数组长度和前一次的比较结果
        cur = mx = 1 + (len(A) > 1)
        
        # 遍历布尔列表，统计最大湍流子数组长度
        for i in range(1, len(arr)):
            if A[i] != A[i+1] and arr[i] != arr[i-1]:
                cur += 1
                mx = max(cur, mx)
            else:
                cur = 2
        
        return mx
