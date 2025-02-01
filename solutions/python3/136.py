
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        输入：包含多个整数的列表 nums。
        输出：返回仅出现一次的数字。
        
        逻辑：
            使用字典记录每个元素出现的次数，最后字典中剩下的那个键就是结果
        """
        # 创建一个空字典来存储数字及其出现次数
        count_dict = {}
        
        # 遍历输入列表，统计每个数字出现的次数
        for num in nums:
            if num not in count_dict:
                count_dict[num] = 1
            else:
                del count_dict[num]
                
        # 返回字典中唯一剩下的键（即只出现一次的那个数字）
        return list(count_dict.keys())[0]
