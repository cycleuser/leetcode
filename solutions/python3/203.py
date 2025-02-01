
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 移除链表中的指定值节点
    def removeElements(self, head: 'ListNode', val: int) -> 'ListNode':
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 使用虚拟头节点简化边界情况处理
        prev, curr = ListNode(None), head

        while curr:
            if curr.val == val:
                # 当前节点值等于目标值，跳过当前节点
                if curr == head:
                    head = head.next
                else:
                    prev.next = curr.next
            elif curr.val != val:
                # 当前节点值不等于目标值，移动指针到下一个节点
                prev = curr

            curr = curr.next

        return head
