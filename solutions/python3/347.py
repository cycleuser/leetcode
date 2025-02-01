    
    class Solution:
        def topKFrequent(self, nums, k):
            """
            :type nums: List[int]  # 输入列表，包含整数
            :type k: int           # 需要返回的高频元素个数
            :rtype: List[int]      # 返回最频繁出现的k个整数
            """
            from collections import Counter as ct  # 引入Counter类用于统计频率
            
            return [key for key, value in ct(nums).most_common(k)]  # 使用Counter统计nums中每个元素的频率，取前k个高频元素
    