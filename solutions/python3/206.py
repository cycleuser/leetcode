
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    定义一个方法来反转单链表。

    参数:
        head: 链表的头节点
        pre: 前一个节点，默认为None，用于记录链表反转时的前驱节点
    
    返回值:
        反转后的链表头节点
    """
    def reverseList(self, head: ListNode, pre = None) -> ListNode:
        # 如果当前节点不为空，则继续递归调用
        if head:
            nex = head.next  # 记录下一个节点
            head.next = pre  # 修改当前节点指向前驱节点
            return self.reverseList(nex, head) if nex else head  # 递归反转剩余链表，直到到达尾节点
