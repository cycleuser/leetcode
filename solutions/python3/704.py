
class Solution:
    # 搜索指定元素在排序数组中的插入位置或返回其索引，如果不存在则返回-1
    
    def search(self, nums: List[int], target: int) -> int:
        # 使用bisect_left查找目标值的位置，如果目标值不在列表中，则返回应插入的左边界索引
        # 双语注释：
        # Search for the index of a target value in a sorted list or return -1 if not found.
        # Use bisect_left to find the position of the target, and return the left insertion point if not present.
        return bisect.bisect_left(nums, target) if target in nums else -1
