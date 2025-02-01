
class Solution:
    # 定义一个方法 findErrorNums，输入是一个整数列表 nums，返回两个整数的列表
    def findErrorNums(self, nums: List[int]) -> List[int]:
        from collections import Counter  # 引入计数器模块

        cnt = Counter(nums)  # 统计每个数字出现的次数
        
        # 首先找到重复的数字，即在计数中出现了两次的数字
        duplicate = [k for k in cnt if cnt[k] == 2]
        
        # 然后找出缺失的数字，即1到nums长度范围内的数字但不在cnt中的数字
        missing = [i for i in range(1, len(nums) + 1) if i not in cnt]

        return duplicate + missing  # 返回重复和缺失的数字列表
