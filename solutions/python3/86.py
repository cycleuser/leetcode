
class Solution:
    # 分类链表 - 将所有小于x的节点放在大于等于x的节点之前
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 创建两个虚拟头节点，用于分别指向小于x和大于等于x的节点列表
        lessHead = less = ListNode(-1)
        greatHead = great = ListNode(-1)

        while head:
            # 将当前节点根据值是否小于x插入到对应的链表中
            if head.val < x:
                less.next = less = head
            else:
                great.next = great = head
            head = head.next

        # 连接两个链表
        less.next, great.next = greatHead.next, None
        
        return lessHead.next  # 返回新的头节点
