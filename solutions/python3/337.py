
class Solution:
    # 定义一个解决方案类

    def rob(self, root):
        # 给定一棵二叉树，实现打家劫舍II：不能同时从两个相邻节点偷窃。

        def dfs(node):
            if not node: 
                return 0, 0  # 如果当前节点为空，则返回两个0
            l, r = dfs(node.left), dfs(node.right)  # 递归处理左子树和右子树

            # 不偷当前节点的最大值
            no_steal = max(l) + max(r)

            # 偷当前节点的总收益，等于左右子树分别不偷的最大值之和加上当前节点的价值
            steal = node.val + l[0] + r[0]

            return no_steal, steal  # 返回两个结果：不偷当前节点的最大值 和 偷当前节点的总收益

        # 最终答案是从dfs(root)返回的结果中取最大值
        return max(dfs(root))
