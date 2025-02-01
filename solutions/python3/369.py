
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 处理链表加1操作
    def plusOne(self, head: 'ListNode') -> 'ListNode':
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # 深度优先遍历，从尾节点开始处理进位
        def dfs(node):
            if not node.next or dfs(node.next):
                if node.val + 1 > 9:
                    node.val = 0
                    return True
                else:
                    node.val += 1
            return False  
        
        # 如果需要在头结点前加一个节点，则返回新链表
        if dfs(head):
            dummy = ListNode(1)
            dummy.next = head
            return dummy
        
        # 否则直接返回原链表
        return head
