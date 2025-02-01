
class Solution:
    # 判断链表中是否存在环
    def hasCycle(self, head: 'ListNode') -> bool:
        # 初始化快慢指针，慢指针从头节点开始，快指针从第二个节点开始（若为空则初始化为None）
        slow, fast = head, head.next if head else None
        
        # 当快慢指针均不为空时继续循环
        while slow != None and fast != None:
            # 如果快慢指针相遇，则表示存在环
            if slow == fast:
                return True
            
            # 更新快慢指针的位置
            slow = slow.next
            fast = fast.next.next if fast.next else None
        
        # 若结束循环后未发现快慢指针相遇，说明无环
        return False
