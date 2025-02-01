
class Solution:
    # Initialize the class-level variable to store the accumulated value
    val = 0

    def bstToGst(self, root):
        """
        Convert a BST (Binary Search Tree) into Greater Sum Tree in-place.
        
        :param root: TreeNode representing the root of the BST
        :return: TreeNode representing the root of the converted Greater Sum Tree
        
        中文注释：
        将二叉搜索树转换为累加树（Greater Sum Tree），在原地进行。
        
        :参数 root: 代表BST根节点的TreeNode对象
        :返回值: 转换后的累加树根节点对应的TreeNode对象
        """
        # Recursively traverse the right subtree first, as it contains larger values
        if root.right:
            self.bstToGst(root.right)
        
        # Update the current node's value to be the sum of its original value and accumulated value
        root.val = self.val = self.val + root.val
        
        # Recursively traverse the left subtree, which will contain smaller or equal values
        if root.left:
            self.bstToGst(root.left)
        
        return root
