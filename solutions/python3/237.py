
class Solution:
    # 删除链表中的节点
    def deleteNode(self, node: ListNode) -> None:
        """
        :type node: ListNode
        :rtype: None. Does not return anything, 
                modifies the linked list in place.
        
        该方法用于删除给定的节点。它通过将当前节点的值设置为下一个节点的值，然后跳过下一个节点来实现。
        这样就相当于移除了下一个节点。
        """
        node.val = node.next.val  # 将当前节点值设为下一节点值
        node.next = node.next.next  # 跳过下一节点，直接指向后继节点
