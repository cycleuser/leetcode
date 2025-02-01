
class Solution:
    # 中文：初始化二分查找的左右指针，分别指向列表的第一个元素和最后一个元素。
    # English: Initialize the left and right pointers for binary search, pointing to the first and last elements of the list.
    
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        # 中文：当左指针小于等于右指针时，继续查找。
        # English: Continue searching while the left pointer is less than or equal to the right pointer.
        
        while l <= r:
            mid = (l + r) // 2
            # 中文：如果中间元素等于目标值，则返回中间索引。
            # English: If the middle element equals the target, return the middle index.
            
            if nums[mid] == target: 
                return mid
            else:
                # 中文：判断目标值与左右边界的关系，调整搜索范围
                # English: Determine the relationship between the target value and the boundaries to adjust the search range
                
                if (target < nums[l], nums[l] <= nums[mid], nums[mid] < target).count(True) == 2:
                    l = mid + 1
                else:
                    r = mid - 1
        # 中文：若未找到目标值，返回-1。
        # English: If the target is not found, return -1.
        
        return -1
