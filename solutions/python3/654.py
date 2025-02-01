
class Solution:
    # 构造最大二叉树 - 中文注释：构造一个从给定整数列表构建的最大二叉树
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int] - 参数说明：输入的整数列表
        :rtype: TreeNode - 返回类型：根节点，构成的最大二叉树
        """
        if nums:
            # 找到最大值及其索引 - 中文注释：找到列表中的最大值及对应的索引位置
            pos = nums.index(max(nums))
            root = TreeNode(nums[pos])  # 构建当前子树的根节点 - 中文注释：以最大值构建当前子树的根节点
            # 递归调用构造左子树 - 中文注释：递归地构造根节点的左子树
            root.left = self.constructMaximumBinaryBinaryTree(nums[:pos])
            # 递归调用构造右子树 - 中文注释：递归地构造根节点的右子树
            root.right = self.constructMaximumBinaryTree(nums[pos+1:])
            return root  # 返回当前子树的根节点 - 中文注释：返回构建好的子树根节点
