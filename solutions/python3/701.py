
class Solution:
    # 定义一个二叉搜索树插入节点的方法，传入根节点root和要插入的值val
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root and root.val > val and not self.insertIntoBST(root.left, val):  # 如果当前节点存在且其值大于val，则递归插入左子树
            # 当前节点的左子节点为新创建的TreeNode(val)，表示已成功插入该节点
            root.left = TreeNode(val)
        elif root and root.val < val and not self.insertIntoBST(root.right, val):  # 如果当前节点存在且其值小于val，则递归插入右子树
            # 当前节点的右子节点为新创建的TreeNode(val)，表示已成功插入该节点
            root.right = TreeNode(val)
        return root  # 返回根节点，表示操作完成
