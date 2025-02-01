
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 中文注释：初始化一个优先队列heap、结果列表res和索引j
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        heap, res, j = [], [], 0
        
        # 中文注释：遍历链表head，直到其为空
        while head:
            # 中文注释：在结果列表中添加0作为初始值
            res.append(0)
            
            # 中文注释：如果堆heap中有元素且最小元素小于当前节点的值，则出堆并更新对应位置的结果
            while heap and heap[0][0] < head.val:
                val, i = heapq.heappop(heap)
                res[i] = head.val
            
            # 中文注释：将当前节点的值和索引j入堆
            heapq.heappush(heap, (head.val, j))
            
            # 中文注释：更新索引j，并移动到下一个节点
            j += 1
            head = head.next
        
        # 中文注释：返回结果列表res
        return res
