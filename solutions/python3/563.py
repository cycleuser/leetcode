
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 计算二叉树的倾斜度
    def findTilt(self, root: 'TreeNode') -> 'int':
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def traverse(node):
            # 如果节点为空，返回0
            if not node:
                return 0
            # 递归计算左子树的值和
            left = traverse(node.left)
            # 递归计算右子树的值和
            right = traverse(node.right)
            # 将左右子树值差的绝对值加入结果列表
            res.append(abs(right - left))
            # 返回当前节点及其子树的值和
            return node.val + left + right
        
        res = []
        # 从根节点开始遍历
        traverse(root)
        # 返回所有倾斜度之和
        return sum(res)
