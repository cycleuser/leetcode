
class Solution:
    """
    定义一个解决方案类，用于寻找满足条件的第k个数。
    
    Class to solve the problem of finding the kth number that meets certain conditions.
    """
    
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        """
        使用二分查找来确定满足条件的最小值。
        
        Use binary search to determine the smallest value that satisfies the condition.
        :param m: 行数
        :param n: 列数
        :param k: 需要找到的第k个数
        :return: 满足条件的最小整数值
        """
        
        # 初始化二分查找的左右边界
        l, r = 1, m * n
        
        while l < r:
            mid = (l + r) // 2
            
            # 计算mid在给定矩阵中的出现次数
            if sum(min(mid // i, n) for i in range(1, m + 1)) < k:
                # 如果总数小于k，说明mid太小了，需要增大左边界
                l = mid + 1
            else:
                # 否则缩小右边界到mid
                r = mid
        
        return l
