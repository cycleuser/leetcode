
class Solution:
    def isCousins(self, root: 'TreeNode', x: int, y: int) -> bool:
        """
        判断二叉树中的两个节点是否为堂兄弟。
        
        :param root: 二叉树根节点
        :param x: 第一个节点值
        :param y: 第二个节点值
        :return: 如果两个节点是堂兄弟，返回True；否则返回False
        
        通过深度优先搜索（DFS）遍历树来找到目标节点x和y。
        """
        
        def dfs(node, parent=None, depth=0):
            """
            深度优先搜索函数，用于递归地在树中查找节点。

            :param node: 当前处理的节点
            :param parent: 当前节点的父节点
            :param depth: 当前节点所在的深度
            """
            if not node:
                return None, None  # 如果当前节点为空，则返回None
            
            if node.val == x or node.val == y:
                # 如果当前节点是目标之一，返回其深度和父节点
                return (depth, parent)
            
            # 递归搜索左子树和右子树
            left_result = dfs(node.left, node, depth + 1)
            if left_result:
                return left_result
            
            right_result = dfs(node.right, node, depth + 1)
            return right_result
        
        dx, px = dfs(root)  # 搜索x所在的深度和父节点
        dy, py = dfs(root)  # 搜索y所在的深度和父节点

        # 如果两个节点的深度相同且父节点不同，则它们是堂兄弟
        return dx == dy and px != py
