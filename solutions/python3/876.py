
class Solution:
    # 定义一个方法middleNode，用于查找链表的中间节点

    def middleNode(self, head: ListNode) -> ListNode:
        # 初始化根节点为head，并设置计数器n为0
        root, n = head, 0
        
        # 遍历链表统计节点数量
        while head:
            head = head.next
            n += 1

        # 移动root到链表中间位置
        for _ in range(n // 2):
            root = root.next

        return root  # 返回中间节点
