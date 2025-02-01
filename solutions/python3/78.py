
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 初始化结果集，包含空集
        # Initialize result set with an empty subset
        res = [[]]
        
        # 遍历每个元素，在当前结果集中添加该元素
        # Iterate over each element and add it to existing subsets in the result set
        for num in nums:
            # 通过列表推导式，将当前结果集中的每个子集与新元素组合成新的子集
            # Use list comprehension to combine current subsets with new elements to form new subsets
            res += [item + [num] for item in res]
        
        # 返回所有可能的子集
        # Return all possible subsets
        return res
