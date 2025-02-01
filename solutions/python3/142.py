
class Solution:
    # 定义检测链表是否存在环及找到入环点的方法
    def detectCycle(self, head: 'ListNode') -> 'ListNode':
        # 初始化快慢指针和根节点指针，都指向头节点
        fast = slow = root = head
        
        # 使用快慢指针法查找相遇点
        while fast and fast.next:
            slow = slow.next       # 慢指针每次移动一步
            fast = fast.next.next  # 快指针每次移动两步
            
            # 当快慢指针相遇时，说明链表存在环
            if slow == fast:
                # 重新定位根节点指针到头节点
                while root != slow: 
                    root = root.next   # 根节点和慢指针都一步一走直到两者相遇
                    slow = slow.next
            
                # 返回入环点
                return root
        
        # 如果没有找到环，返回None
        return None
