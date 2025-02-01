
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        """
        解决航班预定问题。

        参数：
        bookings (List[List[int]]): 预定的区间和人数
        n (int): 航班数量

        返回：
        List[int]: 每个航班预定的人数数组
        """

        # 初始化结果列表，长度为n
        res = [0] * n
        
        # 用于遍历的索引和当前累计值
        i, cur = 0, 0
        
        # 对预定信息进行排序处理
        for j, val in sorted([[i - 1, k] for i, j, k in bookings] + [[j, -k] for i, j, k in bookings]):
            # 增加索引直到遍历到当前预定区间的右边界
            while i < j:
                res[i] = cur
                i += 1
            
            # 更新累计值
            cur += val
        
        return res
