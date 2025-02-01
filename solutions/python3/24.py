
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 交换链表中每两个相邻节点
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        :param head: 链表头节点
        :return: 交换后的链表头节点
        """
        if not head or not head.next: 
            # 如果链表为空或只有一个节点，直接返回头节点
            return head
        
        first = head.next    # 第一个要交换的节点
        second = head        # 当前节点
        second.next = self.swapPairs(first.next)  # 递归处理下一个pair
        first.next = second  # 完成当前pair的交换
        
        return first         # 返回新的头节点
