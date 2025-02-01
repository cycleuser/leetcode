
class Solution:
    # 中文：定义一个方法，用于计算二叉搜索树中值在[L, R]范围内的节点和
    # 英文: Define a method to calculate the sum of node values within range [L, R] in a Binary Search Tree (BST)
    
    def rangeSumBST(self, root, L, R):
        if not root:  # 中文：如果根节点为空，返回0；英文: If the root is None, return 0
            return 0
        
        l = self.rangeSumBST(root.left, L, R)  # 中文：递归计算左子树范围内的节点和；英文: Recursively calculate the sum of nodes within range in the left subtree
        r = self.rangeSumBST(root.right, L, R)  # 中文：递归计算右子树范围内的节点和；英文: Recursively calculate the sum of nodes within range in the right subtree
        
        # 中文：判断当前节点值是否在[L, R]范围内，如果在，则累加当前节点值到结果中
        # 英文: Check if the current node's value is within [L, R], if yes, add its value to the result
        return l + r + (L <= root.val <= R) * root.val
