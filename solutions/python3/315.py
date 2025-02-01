
class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        """
        计算每个元素左侧比其小的元素个数

        Args:
            nums (list[int]): 输入整数列表

        Returns:
            list[int]: 每个元素左侧比其小的元素个数
        """

        # 从后向前遍历，确保插入排序时保持相对顺序
        r = []
        for i in range(len(nums) - 1, -1, -1):
            # 在已有序列表中插入当前值，并返回新位置索引
            bisect.insort(r, nums[i])
            # 计算并更新原列表对应位置为左侧小于当前元素的个数
            nums[i] = bisect.bisect_left(r, nums[i])

        return nums
