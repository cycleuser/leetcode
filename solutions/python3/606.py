
class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        
        英文注释：This function converts a binary tree into a string representation.
        
        中文注释：此函数将二叉树转换为字符串表示形式。
        """
        if not t:
            return ""
        
        # 树节点的值
        parent = str(t.val)
        
        # 左子树部分
        left = ""
        if t.left or t.right:
            left = f"({self.tree2str(t.left)})"
        
        # 右子树部分
        right = ""
        if t.right:
            right = f"(.{self.tree2str(t.right)})"
        
        # 返回完整的字符串表示形式
        return parent + left + right
