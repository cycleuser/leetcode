
class Solution:
    def construct(self, grid):
        """
        构建四叉树。给定一个二维的01矩阵，构建一个四叉树。
        
        :param grid: 二维列表，包含0和1，表示矩阵
        :return: 四叉树根节点
        """

        def dfs(x, y, l):
            """
            深度优先搜索递归构建四叉树。

            :param x: 当前子区域左上角的x坐标
            :param y: 当前子区域左上角的y坐标
            :param l: 当前子区域的边长
            :return: 当前子区域对应的节点
            """
            if l == 1:
                # 如果当前子区域只有一个元素，返回一个叶子结点
                return Node(grid[x][y] == 1, True, None, None, None, None)
            else:
                tLeft = dfs(x, y, l // 2)  # 左上子区域
                tRight = dfs(x, y + l // 2, l // 2)  # 右上子区域
                bLeft = dfs(x + l // 2, y, l // 2)  # 左下子区域
                bRight = dfs(x + l // 2, y + l // 2, l // 2)  # 右下子区域

                value = tLeft.val or tRight.val or bLeft.val or bRight.val  # 当前子树的值

                if (tLeft.isLeaf and
                        tRight.isLeaf and
                        bLeft.isLeaf and
                        bRight.isLeaf and
                        tLeft.val == tRight.val == bLeft.val == bRight.val):
                    # 如果所有子节点都是叶子且值相同，则合并为一个叶子结点
                    return Node(value, True, None, None, None, None)
                else:
                    # 否则，返回当前非叶子结点
                    return Node(value, False, tLeft, tRight, bLeft, bRight)

        if grid:
            # 如果grid不为空，则从(0, 0)开始构建四叉树
            return dfs(0, 0, len(grid))
        else:
            # 否则返回None
            return None
