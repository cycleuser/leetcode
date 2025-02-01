
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 向链表中添加两个数的和
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        left = 0  # 进位值
        dummy = cur = ListNode(-1)  # 哑节点，用于简化返回结果
        
        while l1 or l2 or left:
            # 计算当前位的和及进位
            sm, left = divmod(sum(l and l.val for l in (l1, l2)) + left, 10)
            
            # 创建新的链表节点并连接到结果中
            cur.next = cur = ListNode(sm)
            
            # 移动指针，准备处理下一位
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next  # 返回真正的头节点
