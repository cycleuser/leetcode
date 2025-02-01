
class Solution:
    # 寻找数组中未排序的子数组长度
    
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        arr = sorted(nums)  # 对原数组进行排序
        
        i = 0
        for i in range(len(arr)):
            if arr[i] != nums[i]:  # 找到第一个不匹配的位置
                break
        
        # 从后向前找到最后一个不匹配的位置
        j = len(arr) - 1
        while j >= 0:
            if arr[j] != nums[j]:
                break
            j -= 1
        
        # 计算未排序子数组的长度
        return j - i + 1 if i < j else 0
