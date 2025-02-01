
class Solution:
    """解决方案类"""

    def permuteUnique(self, nums):
        """
        :param nums: 列表，需要进行唯一排列的数字列表
        :return: 列表，包含所有唯一排列组合的结果
        """
        from itertools import permutations  # 导入itertools.permutations用于生成排列

        dic = set()  # 使用集合存储结果以去重
        
        # 遍历生成的所有排列
        for p in permutations(nums):
            if p not in dic: 
                dic.add(p)  # 如果排列未在集合中，则添加进去
            
        return list(dic)  # 将集合转换为列表并返回
