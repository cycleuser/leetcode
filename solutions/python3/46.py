
class Solution:
    """
    中文: 
        实现一个方法来生成给定数字列表的所有排列组合。

    English: 
        Implement a method to generate all permutations of the given number list.
    """

    def permute(self, nums):
        """
        中文: 
            生成给定数字列表的所有排列组合。
        
        English:
            Generate all permutations of the given number list.

        Args:
            nums (List[int]): 输入的数字列表。

        Returns:
            List[tuple]: 返回所有可能的排列组合列表，每个元素是一个元组形式的排列。
        """
        from itertools import permutations
        return list(permutations(nums))
