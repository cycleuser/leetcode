
class Solution:
    def containsDuplicate(self, nums):
        """
        判断给定的整数列表中是否存在重复元素。
        
        :param nums: List[int] - 整数列表
        :return: bool - 如果存在重复返回True，否则返回False
        """
        dic = dict()  # 创建一个字典用于存储已遍历过的数字
        
        for num in nums:
            if not num in dic:  # 检查当前数字是否已在字典中
                dic[num] = 1    # 如果不在，则将其加入字典，值为1表示出现一次
            else:
                return True     # 如果在字典中找到相同数字，说明有重复，返回True
        
        return False           # 遍历完整个列表未发现重复元素，返回False
