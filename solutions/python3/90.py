
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        """
        :type nums: List[int]  # 输入列表，包含整数元素
        :rtype: List[List[int]]  # 返回所有不重复子集组成的列表
        """
        from itertools import combinations as cb
        
        res = []  # 存储结果的列表
        dic = set()  # 用于存储已经处理过的元组，避免重复
        for i in range(len(nums) + 1):
            for item in cb(nums, i):  # 使用itertools.combinations生成所有可能的组合
                item = tuple(sorted(item))  # 将列表转换为排序后的元组
                if item not in dic:  # 检查是否已经处理过此组合
                    dic.add(item)  # 添加到已处理集合中，避免重复
                    res.append(item)  # 将新的子集加入结果列表
        return res  # 返回所有不包含重复的子集组成的列表
