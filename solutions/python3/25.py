
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 反转k个节点的链表
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = last = ListNode(0)  # 创建虚拟头结点和last指针
        cur = head                  # 当前处理的起始节点

        while cur:
            first, cnt = cur, 1      # 记录当前起始节点，计数器置为1
            
            # 检查剩余是否达到k个节点
            while cnt < k and cur:
                cur, cnt = cur.next, cnt + 1
                
            if cnt == k and cur:      # 如果正好有k个节点
                cur, prev = first, None  # 当前头结点，初始化prev为None

                for _ in range(k):       # 反转k个节点
                    next_node = cur.next    # 保存当前节点的下一个节点
                    cur.next, prev, cur = prev, cur, next_node
                
                last.next, last = prev, first  # 更新last和链表结构
            
            else:
                last.next = first        # 不足k个节点，直接连接

        return dummy.next              # 返回新的头结点
