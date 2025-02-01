
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x  # 节点值
        self.next = None  # 指向下一个节点的指针

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 如果l1为空，返回l2
        if not l1:
            return l2
        # 如果l2为空，返回l1
        elif not l2:
            return l1
        # 比较两个节点的值，较小者作为新链表的一部分
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)  # 递归合并剩余部分
            return l1  # 返回当前较小节点
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)  # 递归合并剩余部分
            return l2  # 返回当前较小节点
