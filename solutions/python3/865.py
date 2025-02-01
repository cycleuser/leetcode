
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    定义一个解决方案类，用于找到二叉树中最深叶子节点的所有公共父节点。
    """

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        # 初始化最大深度和结果集
        self.l = 0
        self.nodes = set()
        self.res = None

        """
        使用深度优先搜索（DFS）遍历二叉树，记录最深叶子节点的值及其最大深度。
        """

        def dfs(node, l):
            if node:
                # 如果当前深度大于已知最大深度，则更新最大深度和结果集
                if l > self.l:
                    self.nodes = {node.val}
                    self.l = l
                elif l == self.l:
                    self.nodes.add(node.val)
                # 递归遍历左子树和右子树，增加当前节点的层级深度
                dfs(node.left, l + 1)
                dfs(node.right, l + 1)

        """
        第二次DFS用于确定包含最深叶子节点所有公共父节点的子树。
        """

        def dfs2(node):
            if not node: return set()
            # 获取左子树和右子树的结果集
            l = dfs2(node.left)
            r = dfs2(node.right)
            # 将当前节点值加入结果集中
            total = l | r | {node.val}
            # 检查当前节点是否为最深叶子节点的公共父节点
            if total & self.nodes == self.nodes:
                self.res = node
                return set()
            return total

        dfs(root, 0)  # 第一次DFS遍历树，确定最深叶子节点值及其最大深度
        dfs2(root)    # 第二次DFS找出包含所有最深叶子节点的公共父节点子树
        return self.res  # 返回结果
