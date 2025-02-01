
class Solution:
    # 定义一个移除链表倒数第 n 个节点的方法
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 创建哑结点，方便操作，返回结果时不包含哑结点
        dummy = ListNode(0)
        dummy.next = head
        arr = [dummy]  # 存储节点列表
        
        # 遍历链表，将所有节点加入数组中
        while head:
            arr.append(head)
            head = head.next
        
        # 移除倒数第 n 个节点
        for _ in range(n + 1):
            pre = arr.pop()
        
        # 调整指针指向
        pre.next = pre.next.next
        
        # 返回结果，跳过哑结点
        return dummy.next
