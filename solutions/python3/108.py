
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x  # 节点值
        self.left = None  # 左子节点
        self.right = None  # 右子节点

class Solution:
    def sortedArrayToBST(self, nums):  # 将有序数组转换为二叉搜索树
        """
        :type nums: List[int]  # 输入的有序整数列表
        :rtype: TreeNode  # 返回的根节点，构成的二叉搜索树
        """
        
        if not nums:  # 如果输入列表为空，返回None
            return
        
        mid = len(nums) // 2  # 找到中间索引作为当前子数组的根节点
        root = TreeNode(nums[mid])  # 创建根节点

        # 递归构建左子树
        root.left = self.sortedArrayToBST(nums[:mid])
        
        # 递归构建右子树
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        
        return root  # 返回根节点，完成二叉搜索树构建
