
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 使用两个指针，i 用于遍历数组，items 记录0的个数
        i, items = 0, 0
        
        while i < len(nums) and items <= len(nums):
            # 当前元素为0时，将0移到列表末尾并调整i的位置
            if nums[i] == 0:
                nums.append(0)
                nums.pop(i)
                i -= 1
            
            i += 1
            items += 1
