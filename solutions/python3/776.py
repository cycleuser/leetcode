
class Solution:
    # 定义一个类来解决二叉搜索树的分割问题

    def splitBST(self, root, V):
        """
        :param root: 二叉搜索树的根节点
        :param V: 分割值
        :return: 返回两个二叉搜索树，第一个是小于等于V的子树，第二个是大于V的子树
        """

        # 如果当前节点为空，则返回两个空子树
        if not root:
            return [None, None]

        # 当前节点值等于分割值的情况
        if root.val == V:
            # 将当前节点的右子树分离出来作为大于部分
            a = root.right
            # 清除当前节点的右子树指针
            root.right = None
            return [root, a]

        # 当前节点值小于分割值的情况
        elif root.val < V:
            # 递归处理右子树
            small, large = self.splitBST(root.right, V)
            # 将当前节点的右子树指针指向小于部分
            root.right = small
            return [root, large]

        # 当前节点值大于分割值的情况
        else:
            # 递归处理左子树
            small, large = self.splitBST(root.left, V)
            # 将当前节点的左子树指针指向大于部分
            root.left = large
            return [small, root]
