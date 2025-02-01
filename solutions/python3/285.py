
class Solution:
    # 中文注释：定义一个方法 inorderSuccessor，用于寻找二叉搜索树中给定节点的后继节点。
    # 英文注释: Define a method inorderSuccessor to find the in-order successor of a given node in a binary search tree.
    
    def inorderSuccessor(self, root: "TreeNode", p: "TreeNode") -> "TreeNode":
        if not root:
            return  # 中文注释：如果根节点为空，直接返回 None。
                     # 英文注释: If the root is None, return None.

        if root.val > p.val:
            # 中文注释：如果当前节点值大于给定节点值，则后继可能在左子树中（或左子树的最右节点）。
                     # 英文注释: If current node value is greater than the given node's value, the successor might be in the left subtree (or its rightmost node).
            return self.inorderSuccessor(root.left, p) or root
        else:
            # 中文注释：否则后继节点在右子树中，递归查找。
                     # 英文注释: Otherwise, the successor is in the right subtree, recursively search there.
            return self.inorderSuccessor(root.right, p)
