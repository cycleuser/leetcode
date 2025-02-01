
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 合并k个排序链表
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q = []
        # 遍历所有链表，将节点值加入优先队列q中，并更新链表指针
        for li in lists:
            while li:
                q.append(li)
                li = li.next
        
        root = cur = ListNode()  # 创建新的链表头结点
        # 按照节点的val值从小到大排序，依次构建新链表
        for node in sorted(q, key=lambda x: x.val):
            cur.next = node
            cur = cur.next
        
        return root.next  # 返回合并后的链表头部
