
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        中文注释：
        1. 使用二分查找优化寻找最长递增子序列的长度。
        2. `tails` 数组用于存储当前所有递增子序列中最后一个元素的最小值。
        3. `size` 表示当前能构造的最大递增子序列的长度。
        
        英文注释：
        1. Use binary search to optimize finding the length of the longest increasing subsequence.
        2. The `tails` array stores the minimum values of the last elements in all current increasing subsequences.
        3. `size` indicates the maximum length of the increasing subsequence that can be constructed currently.
        """
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            # 使用二分查找在 tails 中找到第一个大于等于 x 的位置 i
            # Chinese: Use binary search to find the first position `i` where `tails[i] >= x`
            # English: Use binary search to find the first position `i` where `tails[i] >= x`
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            # 更新 size，确保它总是表示当前最大子序列长度
            # Chinese: Update `size` to always indicate the current maximum subsequence length
            # English: Update `size` to always indicate the current maximum subsequence length
            size = max(i + 1, size)
        return size
