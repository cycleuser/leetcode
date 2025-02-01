
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 处理单链表，将奇数位置节点和偶数位置节点分离
    def oddEvenList(self, head: 'ListNode') -> 'ListNode':
        root, i, last, first = head, 1, None, None  # 初始化指针和计数器
        if head and head.next: first = head.next   # 获取第一个偶数节点
        
        while head:
            latter = head.next                   # 当前节点的后继节点
            if i % 2 != 0: last = head           # 奇数位置节点连接到last指针上
            
            if head.next: head.next = head.next.next  # 跳过一个偶数节点
        
            head, i = latter, i + 1              # 更新当前节点和计数器
        
        if last: last.next = first               # 将奇数位置节点与偶数位置节点相连
        
        return root                              # 返回重组后的链表头
