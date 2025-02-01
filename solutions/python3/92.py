
class Solution:
    # 定义一个辅助节点，用于在链表头部进行操作
    def reverseBetween(self, head, m, n):
        # 添加虚拟头节点方便处理边界情况
        dummy_left, dummy_left.next, i = ListNode(0), head, 1

        prev = dummy_left
        while head:
            latter = head.next
            
            # 如果m和n相同，无需反转直接退出循环
            if m == n: 
                break

            # 当i等于m时记录反转起始节点及其前一个节点
            if i == m: 
                head_left, right = prev, head

            # 当i等于n时记录反转结束后的下一节点和当前节点作为结束点
            if i == n: 
                head_right, left = head.next, head
            
            # 在m到n之间进行链表反转操作
            if m < i <= n:
                head.next = prev

            # 更新指针位置，继续遍历下一个节点
            prev, head, i = head, latter, i + 1
        
        # 如果区间存在则完成链表的连接
        if m != n: 
            head_left.next, right.next = left, head_right

        return dummy_left.next
