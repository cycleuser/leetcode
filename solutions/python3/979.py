
class Solution:
    def distributeCoins(self, root):
        """
        分发硬币问题：给定一棵二叉树，每个节点包含整数（可能为负、零或正）。目标是确保每个节点的值恰好为1，
        同时尽量减少从根到叶的所有路径上移动硬币的总次数。
        
        方法：
        - 使用深度优先搜索 (DFS) 来遍历树，并计算需要调整的硬币数量。
        - 对于每个节点，计算其左子树和右子树的硬币不平衡情况（即多余的或缺少的硬币数）。
        - 更新全局变量 `self.ans` 以记录总的硬币移动次数。

        参数:
        root (TreeNode): 二叉树的根节点

        返回值:
        int: 调整至每个节点值为1所需的最小硬币移动次数
        """
        
        self.ans = 0

        def dfs(node):
            """
            深度优先搜索辅助函数
            
            参数:
            node (TreeNode): 当前处理的树节点

            返回值:
            int: 当前节点及其子树的硬币不平衡情况（多余或缺少的硬币数）
            """
            if not node: return 0
            L, R = dfs(node.left), dfs(node.right)
            self.ans += abs(L) + abs(R)
            return node.val + L + R - 1

        dfs(root)
        return self.ans
