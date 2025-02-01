
class Solution:
    def wiggleSort(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # 遍历数组，按照奇偶位置进行调整
        for i in range(0, n - 1, 2):
            if i == n - 2:  # 如果是最后一个元素前的一个元素
                # 检查最后两个元素的顺序是否符合要求
                if nums[-1] < nums[-2]:
                    nums[-2], nums[-1] = nums[-1], nums[-2]
            else:
                # 检查当前元素和下一个元素的相对大小关系，决定是否交换
                if (nums[i + 2] >= nums[i + 1] and nums[i + 1] < nums[i]) or \
                        (nums[i] > nums[i + 2] and nums[i + 2] <= nums[i + 1]):
                    # 根据条件进行元素交换
                    if nums[i + 2] > nums[i + 1]:
                        nums[i + 1], nums[i + 2] = nums[i + 2], nums[i + 1]
                    else:
                        nums[i], nums[i + 1] = nums[i + 1], nums[i]

                    # 这里也可以直接进行交换，简化逻辑
