
class Solution:
    # 定义一个类来解决计数区间和问题

    def countRangeSum(self, nums, lower, upper):
        """
        计算数组中满足特定条件的子数组数量。

        参数:
            nums (List[int]): 输入整数列表。
            lower (int): 区间下限。
            upper (int): 区间上限。

        返回:
            int: 满足条件的子数组数量。
        """
        
        sums, sm, res = [0], 0, 0
        # 初始化前缀和列表、当前累积和sm以及结果计数器res

        for num in nums:
            sm += num  # 更新当前累积和
            # 计算满足条件的子数组数量，使用二分查找加速计算过程
            res += bisect.bisect_right(sums, sm - lower) - bisect.bisect_left(sums, sm - upper)
            
            bisect.insort(sums, sm)  # 插入新的累积和到前缀和列表中保持有序
        return res  # 返回满足条件的子数组数量




class Solution:
    def countRangeSum(self, nums, lower, upper):
        
        sums, sm, res = [0], 0, 0
        
        for num in nums:
            sm += num 
            res += bisect.bisect_right(sums, sm - lower) - bisect.bisect_left(sums, sm - upper)
            bisect.insort(sums, sm)
        return res
