
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 找到最深叶子节点的最近公共祖先
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        # 辅助函数，返回子树的最大深度和该最大深度下的最近公共祖先
        def helper(root):
            if not root:
                return 0, None  # 空节点时，深度为0，公共祖先是None
            
            d1, lca1 = helper(root.left)   # 左子树的深度与最近公共祖先
            d2, lca2 = helper(root.right)  # 右子树的深度与最近公共祖先

            if d1 > d2:    # 比较左右子树的深度
                node = lca1  # 如果左子树更深，则当前节点为左子树最深叶子结点的最近公共祖先
            elif d1 < d2:
                node = lca2  # 右子树更深，右子树的情况同理
            else:   # 深度相同，说明当前节点就是最深叶子节点的最近公共祖先
                node = root

            return max(d1, d2) + 1, node    # 返回较大深度加1及对应的最近公共祖先
        
        # 调用辅助函数，并返回结果中的最近公共祖先
        return helper(root)[1]
