
class Solution:
    def nextPermutation(self, nums):
        # 寻找第一个从后向前递减的元素位置 l
        # Find the first element from right to left that is smaller than its right neighbor
        perm, l = False, len(nums) - 2
        
        while 0 <= l:
            # 寻找比 l 元素大的最右元素 r
            # Find the rightmost element that is larger than nums[l]
            r = len(nums) - 1  
            while l < r and nums[r] <= nums[l]: 
                r -= 1
            
            if r <= l: 
                # 如果没有找到更大的元素，则 l 左移一位
                # If no such element found, move l left one step
                l -= 1
            else:
                # 交换 l 和 r 元素的位置，并对剩余部分进行排序，生成下一个排列
                # Swap nums[l] and nums[r], sort the remaining part to get the next permutation
                nums[l], nums[l + 1:], perm = nums[r], sorted(nums[l + 1:r] + [nums[l]] + nums[r + 1:]), True
                break
        
        if not perm:
            # 如果没有找到下一个排列，则将整个数组排序
            # If no next permutation found, sort the whole array
            nums.sort()
