
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]  # 输入的整数列表
        :rtype: List[int]      # 返回缺失的数字列表
        """
        return [x for x in set(range(1, len(nums) + 1)) - set(nums)]  # 使用集合操作找出缺失的数字
