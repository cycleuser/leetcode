
class Solution:
    # 定义一个类来解决问题
    
    def smallestRangeII(self, A: list[int], K: int) -> int:
        """
        计算将数组A中的每个元素增加或减少K后，得到的范围内最大差值最小的范围。
        
        参数:
            A (list[int]): 输入的整数列表
            K (int): 可以对每个元素进行增减的最大值
        
        返回:
            int: 通过调整后的最小范围
        """
        
        # 对数组A进行排序，方便后续操作
        A.sort()
        
        # 计算原始最大差值作为初始最小范围
        min_range = A[-1] - A[0]
        
        # 遍历数组，计算调整后的可能最小范围
        for i in range(len(A) - 1):
            max_val = max(A[-1] - K, A[i] + K)
            min_val = min(A[0] + K, A[i + 1] - K)
            
            # 计算当前范围内最大差值，并更新最小范围
            min_range = min(min_range, max_val - min_val)
        
        return min_range



class Solution:
    def smallestRangeII(self, A: list[int], K: int) -> int:
        """
        计算将数组A中的每个元素增加或减少K后，得到的范围内最大差值最小的范围。
        
        参数:
            A (list[int]): 输入的整数列表
            K (int): 可以对每个元素进行增减的最大值
        
        返回:
            int: 通过调整后的最小范围
        """
        A.sort()
        min_range = A[-1] - A[0]
        
        for i in range(len(A) - 1):
            max_val = max(A[-1] - K, A[i] + K)
            min_val = min(A[0] + K, A[i + 1] - K)
            
            min_range = min(min_range, max_val - min_val)
        
        return min_range
