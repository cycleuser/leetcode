
class Solution:
    def smallestFromLeaf(self, root: 'TreeNode', s = '') -> str:
        # 中文注释：如果当前节点没有左右子节点，返回由当前节点值组成的字符与s拼接后的字符串
        if not root.right and not root.left:
            return chr(97 + root.val) + s
        
        # 中文注释：如果当前节点只有右子节点，递归调用左子树，并将当前节点的字符添加到s中
        if not root.right:
            return self.smallestFromLeaf(root.left, chr(97 + root.val) + s)
        
        # 中文注释：如果当前节点只有左子节点，递归调用右子树，并将当前节点的字符添加到s中
        if not root.left:
            return self.smallestFromLeaf(root.right, chr(97 + root.val) + s)
        
        # 中文注释：如果当前节点有左右子节点，分别递归处理左右子树，并返回较小的结果
        return min(self.smallestFromLeaf(root.left, chr(97 + root.val) + s), self.smallestFromLeaf(root.right, chr(97 + root.val) + s))
