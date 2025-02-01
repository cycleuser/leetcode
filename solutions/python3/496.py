
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]  # 输入列表 nums1，包含整数
        :type nums2: List[int]  # 输入列表 nums2，包含整数
        :rtype: List[int]       # 返回值为与 nums1 长度相同的结果列表
        
        解题思路：对于 nums1 中的每个元素，在 nums2 中查找第一个大于它的元素。
                  如果找到，则记录该元素；如果未找到，则记录 -1。
        """
        out = list()
        
        for num in nums1:
            # 初始化为-1，表示默认找不到下一个更大元素
            out.append(-1)
            
            # 从 nums2 中对应元素的下一个位置开始查找
            for j in range(nums2.index(num) + 1, len(nums2)):
                if nums2[j] > num: 
                    out[-1] = nums2[j]
                    break
        
        return out
