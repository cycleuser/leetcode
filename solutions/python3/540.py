
class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]  # 输入的列表nums，包含多个整数
        :rtype: int           # 返回一个整数，即列表中唯一的非重复元素
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if mid + 1 < len(nums) and nums[mid] == nums[mid + 1]:
                # 如果mid和mid+1相等，说明非重复元素在右半部分
                if mid % 2 == 0:
                    left = mid + 2
                else:
                    right = mid - 1
            elif mid - 1 >= 0 and nums[mid] == nums[mid - 1]:
                # 如果mid和mid-1相等，说明非重复元素在左半部分
                if mid % 2 == 0:
                    right = mid - 2
                else:
                    left = mid + 1
            else:
                return nums[mid]
