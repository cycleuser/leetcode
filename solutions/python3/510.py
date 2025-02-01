
class Solution:
    # 定义查找二叉搜索树中序后继节点的方法
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        # 如果当前节点有右子树，则找其最左下的节点作为后继
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        
        # 从给定节点开始，向上查找父节点直到找到一个节点是其父节点的左子节点为止
        while node.parent and node.parent.left != node:
            node = node.parent
        # 返回最后一个满足条件的父节点作为后继
        return node.parent
