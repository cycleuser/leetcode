
class Solution:
    # 判断目标元素在列表中出现次数是否超过总长度的一半

    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        # 使用count方法统计目标值出现的次数，如果大于列表长度的一半则返回True
        return nums.count(target) > len(nums) // 2
