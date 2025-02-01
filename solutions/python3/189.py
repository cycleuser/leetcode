
class Solution:
    # 用于旋转数组中的元素，不返回新列表，而是直接修改原地的nums列表
    def rotate(self, nums: list[int], k: int) -> None:
        """
        :type nums: List[int]  # 输入是一个整数列表
        :type k: int           # k是需要旋转的次数
        :rtype: void           # 不返回任何值，直接修改输入的nums列表
        """
        
        n = k % len(nums)    # 计算实际需要旋转的位置数量
        
        # 通过切片操作重新组合数组内容并覆盖原数组
        nums[:] = nums[-n:] + nums[:-n]
