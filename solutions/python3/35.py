
class Solution:
    # 搜索插入位置 - Search Insert Position
    
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 使用 bisect_left 方法找到目标值应插入的位置，保持原有序列不变
        return bisect.bisect_left(nums, target)
