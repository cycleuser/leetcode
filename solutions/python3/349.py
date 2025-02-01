
class Solution:
    # 定义一个名为intersection的方法，用于找出两个整数列表的交集
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        :param nums1: 第一个整数列表
        :param nums2: 第二个整数列表
        :return: 两个列表的交集作为整数列表返回
        
        通过将两个列表转换为集合并求交集，然后将结果转换回列表。
        这种方法利用了集合去重和高效查找特性来提高效率。
        """
        return list(set(nums1) & set(nums2))
