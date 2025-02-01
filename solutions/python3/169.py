
class Solution:
    # 定义一个类，用于解决众数问题

    def majorityElement(self, nums):
        """
        :param nums: List[int] - 输入的整数列表
        :return: int - 列表中的众数
        """
        num_list = dict()  # 创建字典用于存储数字及其出现次数
        
        for num in nums:
            if num not in num_list:
                num_list[num] = 1  # 如果数字不在字典中，初始化其计数为1
            else:
                num_list[num] += 1  # 否则，增加该数字的计数
        
        # 返回出现次数最多的那个数字，使用key=num_list.get作为依据
        return max(num_list, key=num_list.get)
