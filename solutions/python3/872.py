
class Solution:
    def leafSimilar(self, root1, root2):
        # 中文注释: 定义一个深度优先搜索辅助函数，用于遍历树并收集叶子节点值
        # English comment: Define a depth-first search helper function to traverse the tree and collect leaf node values
        def dfs(node, arr):
            if node:
                if not node.left and not node.right:  # 中文注释: 判断当前节点是否为叶子节点
                    # English comment: Check if the current node is a leaf node
                    arr += [node.val]  # 中文注释: 如果是叶子节点，将值加入数组
                    # English comment: If it's a leaf node, append its value to the array
                dfs(node.left, arr)  # 中文注释: 递归遍历左子树
                # English comment: Recursively traverse the left subtree
                dfs(node.right, arr)  # 中文注释: 递归遍历右子树
                # English comment: Recursively traverse the right subtree
            return arr

        # 中文注释: 比较两棵树的叶子节点序列是否相同
        # English comment: Compare if the leaf sequences of two trees are the same
        return dfs(root1, []) == dfs(root2, [])
