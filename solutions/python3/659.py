
class Solution:
    def isPossible(self, nums):
        """
        判断给定数组是否可以分解为若干个连续子序列。
        
        :param nums: List[int] - 给定的整数列表
        """
        import heapq  # 引入堆模块

        heap = []  # 初始化空堆
        last = collections.defaultdict(int)  # 记录每个数字出现次数
        
        for num in nums:
            last[num] += 1  # 更新当前数字的计数
            
            if heap and heap[0][0] <= num - 1:  # 堆顶元素小于等于当前数字减一
                if heap[0][0] < num - 1:  # 如果堆顶元素小于当前数字减一，无法形成连续子序列
                    return False
                else:
                    last[num - 1] -= 1  # 更新前一个数字的计数
                    n, l = heapq.heappop(heap)  # 弹出堆顶元素
                    if l == -1:  # 如果该元素已被使用完
                        heapq.heappush(heap, (num, -2))  # 将其更新为-2，表示已结束
                    else:
                        heapq.heappush(heap, (n + 1, l - 1))  # 更新堆顶元素的值和计数
            
            elif num - 1 not in last or not last[num - 1]:  # 如果前一个数字不存在或数量为0
                heapq.heappush(heap, (num, -1))  # 将当前数字加入堆中，标记未使用状态
            else:
                last[num - 1] -= 1  # 更新前一个数字的计数
        
        return not heap  # 如果最终堆为空，则表示所有元素都能形成连续子序列
