
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    判断在二叉树中是否可以进行一次操作使得节点数量大于对手，从而赢得游戏。
    传入参数包括：根节点 root、节点总数 n 和特定目标节点值 x。

    该方法主要逻辑如下：
    - 通过递归计算每个子树的节点数
    - 找到目标节点x所在的子树，并记录左右子树的节点数量c[0]和c[1]
    - 检查剩余部分（非x所在子树）的节点数是否大于等于最大子树节点数加一，以赢得游戏
    """

    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        c = [0, 0]  # 用于记录目标节点x所在子树的左右子树节点数量

        def count(node):
            if not node: 
                return 0
            l, r = count(node.left), count(node.right)
            if node.val == x:
                c[0], c[1] = l, r
            return l + r + 1
        
        # 计算整个树的节点数，同时记录目标子树的信息
        total_nodes = count(root)

        # 判断是否可以通过增加一个节点赢得游戏
        # 需要剩余部分（非x所在子树）大于等于最大子树加一
        return total_nodes // 2 < max(max(c), n - sum(c) - 1)
