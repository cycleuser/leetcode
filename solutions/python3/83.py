
class Solution:
    # 初始化节点
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        :param head: 链表头结点
        :return: 删除重复元素后的链表头结点
        """
        cur = root = head  # 当前指针初始化为根节点和head

        while head:  # 遍历链表
            if head.val != cur.val:  # 如果当前节点值与cur不等
                cur.next = cur = head  # 更新cur指向并移动cur到head的位置
            head = cur.next = head.next  # 移动head指针

        return root  # 返回新的头结点
