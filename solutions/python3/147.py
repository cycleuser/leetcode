
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 使用插入排序对链表进行排序
    def insertionSortList(self, head: 'ListNode') -> 'ListNode':
        ref, ref.next, n = ListNode(float("-inf")), head, 0
        
        while head:
            # 创建新的节点并初始化
            inserted, curr, prev, n = ListNode(head.val), ref.next, ref, n + 1
            
            # 遍历已排序部分，找到插入位置
            for i in range(n - 1):
                if inserted.val < curr.val:
                    prev.next, inserted.next = inserted, curr
                    # 如果是最后一个节点，则断开链表
                    if i >= n - 2: curr.next = None 
                    break
                else:
                    prev, curr = curr, curr.next
            # 移动未排序部分的头指针
            head = head.next
        
        return ref.next
