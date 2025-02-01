
class Solution:
    def verticalTraversal(self, root: 'TreeNode') -> List[List[int]]:
        """
        该方法用于垂直遍历二叉树，并返回按垂直顺序排列的节点值列表。
        
        :param root: 二叉树根节点
        :return: 按垂直顺序排列的节点值列表
        """

        self.arr = []  # 存储节点信息元组 (x坐标, y坐标, 节点值)

        def dfs(node: 'TreeNode', x: int, y: int) -> None:
            """
            深度优先搜索遍历二叉树。

            :param node: 当前遍历到的节点
            :param x: 当前节点在x轴上的坐标
            :param y: 当前节点在y轴上的坐标
            """
            if node:
                self.arr.append((x, y, node.val))  # 记录当前节点信息
                dfs(node.left, x - 1, y + 1)       # 遍历左子树
                dfs(node.right, x + 1, y + 1)      # 遍历右子树

        dfs(root, 0, 0)  # 从根节点开始深度优先搜索

        # 按x坐标排序，然后按y坐标分组，最后提取每个组中的节点值
        return [list(map(lambda x: x[-1], g)) for k, g in itertools.groupby(sorted(self.arr), key=lambda x: x[0])]
