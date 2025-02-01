
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 获取二叉树的边界节点
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root: 
            return []
        
        used, res, r = {root}, [root.val], []  # 初始化已使用节点集合、结果列表和右边界临时列表

        # 获取左边界节点
        def lb(node):
            if node not in used:
                used.add(node)
                res.append(node.val)
            if node.left: 
                lb(node.left)  # 先访问左子树
            elif node.right: 
                lb(node.right)

        # 获取右边界节点
        def rb(node):
            if node not in used:
                used.add(node)
                r.append(node.val)
            if node.right: 
                rb(node.right)  # 先访问右子树
            elif node.left: 
                rb(node.left)

        # 获取叶子节点
        def lv(node):
            if not node.left and not node.right and node not in used:
                used.add(node)
                res.append(node.val)
            if node.left: 
                lv(node.left)
            if node.right: 
                lv(node.right)

        # 处理左边界
        if root.left: 
            lb(root.left)
        
        # 获取叶子节点
        lv(root)
        
        # 处理右边界
        if root.right:
            rb(root.right)
        
        return res + r[::-1]  # 结果加上反转后的右边界列表
