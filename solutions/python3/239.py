
class Solution:
    # 定义一个类来解决滑动窗口最大值的问题
    
    def maxSlidingWindow(self, nums, k):
        import collections
        from heapq import heappush, heappop
        
        cnt = collections.Counter()  # 统计元素出现次数
        heap = []  # 最大堆，用于维护当前窗口的最大值
        res = []   # 存储结果

        for i, num in enumerate(nums):
            # 将当前数的负值加入最大堆，并更新其在计数字典中的计数
            heappush(heap, -num)
            cnt[num] += 1
            
            # 调整堆，确保堆顶元素为当前窗口的最大值
            while not cnt[-heap[0]]:
                heappop(heap)

            # 当遍历到第 k-1 个元素时开始填充结果数组
            if i >= k - 1:
                res.append(-heap[0])  # 将堆顶元素的正值加入结果数组

                # 减少滑动窗口最左边元素的计数，以便在后续迭代中移除它
                cnt[nums[i - k + 1]] -= 1
        
        return res
