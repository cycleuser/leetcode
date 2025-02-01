
class Solution:
    def findMin(self, nums):
        """
        寻找旋转排序数组中的最小值。
        
        在一个旋转排序数组中，部分元素被旋转了。需要找到数组中的最小值。

        Args:
            nums (List[int]): 旋转排序数组

        Returns:
            int: 数组中的最小值
        """

        l, r, res = 0, len(nums) - 1, nums[0] if nums else float('inf')
        while l <= r:
            # 去除重复的左边界
            while l < r and nums[l] == nums[l + 1]: 
                l += 1
            # 去除重复的右边界
            while l < r and nums[r] == nums[r - 1]: 
                r -= 1

            mid = (l + r) // 2
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r, res = mid - 1, min(res, nums[mid])
        return res
