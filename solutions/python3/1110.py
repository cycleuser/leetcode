
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 删除给定值节点的二叉树中指定值的节点，并返回新的树根列表
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        def dfs(node: TreeNode, parent: TreeNode) -> bool:
            """
            深度优先搜索，判断当前节点是否保留或删除
            :param node: 当前处理的节点
            :param parent: 父节点
            :return: 当前节点是否被删除
            """
            if not node:
                return True
            
            # 递归处理左右子树
            dfs(node.left, node)
            dfs(node.right, node)

            # 如果当前节点值在待删除集合中，进行删除操作
            if node.val in blacklist:
                if parent and parent.left == node:
                    parent.left = None
                elif parent:
                    parent.right = None

                # 将子树加入结果集
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)

                return False
            
            return True
        
        res = []
        blacklist = set(to_delete)  # 转换为集合提高查找效率
        dfs(root, None)  # 从根节点开始搜索

        # 如果根节点不被删除，则加入结果集
        if root.val not in blacklist:
            res.append(root)

        return res
