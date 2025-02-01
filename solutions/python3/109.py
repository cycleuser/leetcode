
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 将有序链表转换为二叉搜索树
    # :param head: ListNode 类型，有序链表的头节点
    # :return: TreeNode 类型，构建好的二叉搜索树根节点
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        
        def traverse(arr):
            # 如果数组为空，则返回空节点
            if not arr: return None
            mid_index = len(arr) // 2
            node = TreeNode(arr[mid_index])
            # 递归构建左子树和右子树
            node.left = traverse(arr[:mid_index])
            node.right = traverse(arr[mid_index+1:])
            return node

        # 将链表节点值存入数组中
        array = []
        while head:
            array.append(head.val)
            head = head.next
        
        # 调用辅助函数，构建二叉搜索树
        return traverse(array)
