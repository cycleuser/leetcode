
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # 合并两个有序数组，并排序
        # Merge and sort two sorted arrays
        arr = sorted(nums1 + nums2)
        
        # 如果合并后的数组长度为偶数，则中位数是中间两个数的平均值
        # If the length of merged array is even, median is the average of the two middle numbers
        if len(arr) % 2 == 0:
            return (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2
        
        # 如果合并后的数组长度为奇数，则中位数是中间的那个数
        # If the length of merged array is odd, median is the middle number
        else:
            return arr[len(arr) // 2]
