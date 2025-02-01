
class Solution:

    # 计算节点总数
    def countNodes(self, root):
        """
        :param root: 树的根节点 (Node)
        :return: 树中节点总数 (int)
        """
        if not root:
            return 0
        
        l = self.getDepth(root.left)     # 获取左子树深度
        r = self.getDepth(root.right)    # 获取右子树深度

        if l == r:
            # 如果左右子树深度相同，则节点总数为2^l + 右子树节点数
            return (1 << l) + self.countNodes(root.right)
        
        # 否则，节点总数为2^r + 左子树节点数
        return (1 << r) + self.countNodes(root.left)

    # 获取树的深度
    def getDepth(self, root):
        """
        :param root: 树的根节点 (Node)
        :return: 树的深度 (int)
        """
        if not root:
            return 0
        return 1 + self.getDepth(root.left)     # 深度+1
