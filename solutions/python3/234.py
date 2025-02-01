
class Solution:
    # 检查给定链表是否为回文结构

    def isPalindrome(self, head):
        # 初始化快慢指针，初始时均指向头节点
        r = fast = head
        # 用于反转链表的部分的前驱节点
        l = None
        
        while fast and fast.next:
            # 快指针每次移动两位
            fast = fast.next.next
            # 反转链表操作：将当前节点r连接到l之后，更新l和r指向
            r.next, l, r = l, r, r.next
        
        if fast: 
            # 如果快指针走到底则表示节点数为奇数，此时r需要再向前一步
            r = r.next
        
        # 检查反转后的前半部分链表和未变的后半部分是否相等
        while l and r and l.val == r.val:
            l, r = l.next, r.next
        
        # 如果没有剩余节点，说明是回文结构
        return not l
