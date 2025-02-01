
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x  # 节点值初始化
        self.next = None  # 下一个节点指针初始化

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 将链表中的数值提取到列表中并排序
        ls = []
        while head:
            ls.append(head.val)
            head = head.next
        
        # 如果列表为空，则返回空链表，否则进行后续操作
        if not ls:
            return []

        root = head = ListNode(ls[0])  # 初始化根节点和头指针

        # 遍历排序后的列表，并构建新的有序链表
        for i in range(1, len(ls)):
            head.next = ListNode(ls[i])
            head = head.next
        
        return root
