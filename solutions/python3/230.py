
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x  # 初始化节点值
        self.left = None  # 初始化左子节点为None
        self.right = None  # 初始化右子节点为None

class Solution:
    def __init__(self):
        self.k = 0  # 记录需要寻找的第k小元素的位置
        self.res = None  # 存储结果，即找到的第k小元素

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        寻找二叉搜索树中第k小的节点值。
        
        :param root: 树根节点
        :param k: 需要寻找的第k小节点的位置
        :return: 第k小的节点值
        """

        # 递归遍历左子树，找到第k小的元素
        if self.k < k and root.left:
            self.kthSmallest(root.left, k)
        
        # 计数器加一，并检查是否已经找到了第k个元素
        self.k += 1

        # 如果是第k个元素，则记录其值
        if self.k == k:
            self.res = root.val
        
        # 继续递归遍历右子树，找到第k小的元素
        if self.k < k and root.right:
            self.kthSmallest(root.right, k)
        
        return self.res  # 返回结果
