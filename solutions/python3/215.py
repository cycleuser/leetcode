
class Solution:
    # 寻找数组中第k大的元素

    def findKthLargest(self, nums, k):
        # 使用heapq的nlargest方法找到前k个最大的数，返回其中最小的一个即为所求
        return heapq.nlargest(k, nums)[-1]
