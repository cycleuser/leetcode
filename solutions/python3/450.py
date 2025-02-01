
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 二叉树节点删除操作
    def deleteNode(self, root: 'TreeNode', key: int) -> 'TreeNode':
        if not root: return
        
        # 当前结点值大于key，递归到左子树并更新当前结点的左子树引用
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        
        # 当前结点值小于key，递归到右子树并更新当前结点的右子树引用
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        
        # 找到要删除的节点
        else:
            # 无右子树或左子树情况处理
            if not root.right: return root.left
            elif not root.left: return root.right
            
            # 寻找右子树最小结点并替换当前结点值，递归更新右子树
            tmp, mini = root.right, root.right.val
            while tmp.left:
                tmp, mini = tmp.left, tmp.left.val
            root.val, root.right = mini, self.deleteNode(root.right, mini)
        
        return root
