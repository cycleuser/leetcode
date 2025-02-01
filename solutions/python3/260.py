
class Solution:
    # 用于找出数组中出现一次的两个数字
    
    def singleNumber(self, nums):
        """
        :param nums: List[int] - 输入整数列表
        :return: List[int] - 返回出现一次的两个整数
        
        示例:
        >>> s = Solution()
        >>> s.singleNumber([1, 2, 1, 3, 2, 5])
        [3, 5]
        
        思路：
        使用collections.Counter来统计每个数字出现的次数，然后获取出现一次的两个数字
        """
        from collections import Counter
        
        # 统计每个元素出现的频率
        num_counts = Counter(nums)
        
        # 获取出现一次的两个数字
        result = [num for num, count in num_counts.items() if count == 1]
        
        return result
