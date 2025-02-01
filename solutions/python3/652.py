
class Solution:
    # 寻找二叉树中的重复子树

    def findDuplicateSubtrees(self, root):
        """
        :param root: TreeNode, 树的根节点
        :return: List[TreeNode], 包含所有重复子树的根节点列表
        """

        def dfs(root):
            # 如果当前节点为空，返回'null'
            if not root:
                return "null"
            # 构建子树结构字符串
            struct = "%s,%s,%s" % (str(root.val), dfs(root.left), dfs(root.right))
            # 将当前子树结构与对应的节点加入字典
            nodes[struct].append(root)
            return struct

        # 使用defaultdict存储子树结构及其对应的节点列表
        nodes = collections.defaultdict(list)
        # 从根节点开始进行深度优先搜索
        dfs(root)
        # 返回所有出现多次的子树的首个节点
        return [nodes[struct][0] for struct in nodes if len(nodes[struct]) > 1]
