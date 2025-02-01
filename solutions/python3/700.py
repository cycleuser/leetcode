
class Solution:
    # 中文：搜索二叉树，给定节点root和目标值val，在二叉搜索树中查找等于val的节点。
    # 英文：Search a Binary Search Tree (BST), given node `root` and target value `val`.
    def searchBST(self, root, val):
        if root and val < root.val:  # 中文：如果当前节点存在且目标值小于当前节点值，则递归搜索左子树。
            # 英文：If the current node exists and the target value is less than the current node's value,
            # recursively search the left subtree.
            return self.searchBST(root.left, val)
        elif root and val > root.val:  # 中文：如果当前节点存在且目标值大于当前节点值，则递归搜索右子树。
            # 英文：If the current node exists and the target value is greater than the current node's value,
            # recursively search the right subtree.
            return self.searchBST(root.right, val)
        return root  # 中文：如果找到等于目标值的节点或遍历到叶子节点，则返回当前节点。
        # 英文：Return the current node if a node with the target value is found or reach a leaf node.
