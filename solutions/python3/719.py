
class Solution(object):
    # 计算数组中差值不超过给定值的对数
    def countPairsLTE(self, array, value):
        # 使用bisect_right查找大于array[i] + value的第一个位置，减去i和1得到满足条件的对数
        return sum(bisect.bisect_right(array, array[i] + value, lo=i) - i - 1 for i in range(len(array)))
    
    # 找到差值小于等于k的第k个最小值
    def smallestDistancePair(self, nums, k):
        # 对数组进行排序，方便后续二分查找
        nums.sort()
        
        # 初始化low和high，分别为相邻元素最大差值和整个数组的最大差值
        low, high = min([nums[i + 1] - nums[i] for i in range(len(nums) - 1)]), nums[-1] - nums[0]
        
        # 二分查找过程
        while low < high:
            mid = (low + high) // 2
            
            # 判断mid是否满足条件：差值不超过mid的对数是否大于等于k
            if self.countPairsLTE(nums, mid) < k:
                low = mid + 1
            else:
                high = mid
        
        # 返回最终结果
        return low
