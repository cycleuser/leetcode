
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 重新排序链表，将节点按顺序交错排列
    def reorderList(self, head: ListNode) -> None:
        if head:
            arr = []
            # 将链表节点值存入数组
            while head:
                arr += head,
                head = head.next
            
            l, r, prev = 0, len(arr) - 1, ListNode(0)
            # 使用双指针从两端交替插入
            while l < r:
                prev.next, arr[l].next, prev, l, r = arr[l], arr[r], arr[r], l + 1, r - 1
            
            # 处理奇数个节点的情况
            if l == r: 
                prev.next = arr[l]
            
            # 断开重新连接后的链表末尾，防止形成环
            arr[l].next = None
