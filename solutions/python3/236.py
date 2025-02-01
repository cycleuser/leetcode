
class Solution:
    # 寻找二叉树中两个节点的最近公共祖先

    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        # 使用字典记录每个节点的父节点，并使用栈进行深度优先搜索
        parent, stack = {root: None}, [root]
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # 使用集合记录p的祖先节点
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]

        # 找到q的最近公共祖先
        while q not in ancestors:
            q = parent[q]
        return q
