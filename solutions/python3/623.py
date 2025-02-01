
class Solution:
    def addOneRow(self, root: 'TreeNode', v: int, d: int) -> 'TreeNode':
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        
        # 初始化队列和深度计数器
        q, depth = [root], 1
        
        # 遍历至目标插入行的父节点所在的层级
        while depth != d:
            parent, q, depth = q, [kid for node in q for kid in (node.left, node.right) if kid], depth + 1
        
        # 当插入行不在根节点时，创建新节点并连接到原树
        if d != 1:
            for node in parent:
                node.left, node.right = TreeNode(v), TreeNode(v)
                node.left.left, node.right.right = node.left, node.right
            return root
        
        # 当插入行为根节点所在的行时，创建新根节点并连接原树
        else: 
            first = TreeNode(v); first.left = root
            return first
