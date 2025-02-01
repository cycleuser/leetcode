
class Solution:
    res = 0

    # 计算最少需要安装的摄像头数量以覆盖所有节点
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # 深度优先搜索，返回当前节点的状态
        def dfs(root):
            if not root:
                return 2  # 空节点，状态为可覆盖

            left = dfs(root.left)
            right = dfs(root.right)

            # 如果左或右子树中有一个未被覆盖，则需要安装一个摄像头
            if left == 0 or right == 0:
                self.res += 1
                return 1  # 安装了摄像头，状态为已覆盖

            # 如果当前节点的左右子树都被覆盖，则返回2表示可覆盖
            if left == 1 or right == 1:
                return 2

            # 否则，返回0表示未被覆盖
            return 0

        # 最终结果：根节点自身未被覆盖的情况下需要额外增加一个摄像头
        return (dfs(root) == 0) + self.res
