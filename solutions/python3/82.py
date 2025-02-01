
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 删除链表中的重复元素，返回新的无重复节点的链表头结点
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy_left = ListNode(0)  # 哑节点
        dummy_left.next = head   # 将哑节点指向原链表头结点

        prev, prev_num = None, dummy_left  # 初始化前一个节点和前一个节点的前驱节点
        
        while head:  # 遍历整个链表
            if prev and prev.val != head.val: 
                prev_num = prev  # 更新前驱节点
            
            if prev and prev.val == head.val:
                while head and head.next and head.next.val == head.val: 
                    head = head.next  # 跳过重复节点
                head = head.next
                prev_num.next = head  # 调整指针，跳过重复节点

            prev = head  # 更新前一个节点
            if head: 
                head = head.next  # 向后移动当前节点
        
        return dummy_left.next  # 返回新链表的头结点
