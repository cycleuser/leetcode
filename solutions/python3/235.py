
class Solution:
    # 定义一个函数用于查找二叉搜索树的最近公共祖先节点
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # 如果p和q的值分别位于root左右，则当前root即为所求
        if p.val < root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # 如果p和q的值分别位于root右左，则当前root即为所求
        if p.val > root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        # 返回当前节点作为最近公共祖先
        return root
