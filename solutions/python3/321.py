
class Solution:
    # 定义一个方法来合并两个数组，返回一个新的最大数数组
    def merge(self, arr1, arr2):
        # 初始化结果列表和指针
        res, i, j = [], 0, 0
        
        # 当两个子数组都有剩余元素时循环
        while i < len(arr1) and j < len(arr2):
            # 比较剩余部分的大小，将较大的数加入结果中
            if arr1[i:] >= arr2[j:]:
                res.append(arr1[i])
                i += 1
            else: 
                res.append(arr2[j])
                j += 1
        
        # 将未处理完的子数组剩余部分添加到结果列表
        if i < len(arr1): res += arr1[i:]
        elif j < len(arr2): res += arr2[j:]
        
        return res
    
    # 定义一个方法来构造最大数数组
    def makeArr(self, arr, l):
        i, res = 0, []
        for r in range(l - 1, -1, -1):
            num, i = max(arr[i:-r] or arr[i:])
            i = -i + 1
            res.append(num)
        return res
    
    # 主方法，寻找两个数组合并后的最大k长度子数组
    def maxNumber(self, nums1, nums2, k):
        # 将原始数组转换为包含索引的元组列表，并反转排序
        nums1, nums2, choices = [(num, -i) for i, num in enumerate(nums1)], [(num, -i) for i, num in enumerate(nums2)], []
        
        # 遍历所有可能的选择组合
        for m in range(k + 1):
            if m > len(nums1) or k - m > len(nums2): continue
            
            # 构造两个数组并合并它们
            arr1, arr2 = self.makeArr(nums1, m), self.makeArr(nums2, k - m)
            choices.append(self.merge(arr1, arr2))
        
        # 返回所有组合中的最大值
        return max(choices)
