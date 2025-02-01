
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        """
        检查并修剪树，使得所有从根到叶的路径上的节点值之和至少为给定的限制。
        
        :param root: 树的根节点
        :type root: TreeNode
        :param limit: 限制值
        :type limit: int
        :return: 经过修剪后的树的根节点
        :rtype: TreeNode
        """
        if not root.left and not root.right:
            # 如果当前节点没有子节点，检查其值是否满足限制条件
            return None if root.val < limit else root
        
        if root.left:
            # 递归处理左子树，并更新路径和
            root.left = self.sufficientSubset(root.left, limit - root.val)
        
        if root.right:
            # 递归处理右子树，并更新路径和
            root.right = self.sufficientSubset(root.right, limit - root.val)
        
        # 如果当前节点的左右子节点都被修剪掉，则返回None，表示该节点可以被移除
        return root if root.left or root.right else None
