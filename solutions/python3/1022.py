
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 计算从根节点到叶子节点的二进制数值之和模10^9+7
    def sumRootToLeaf(self, r: TreeNode, num = 0) -> int:
        if not r: 
            return 0
        
        # 将当前节点值加入路径数值中，并左移一位
        num = (num << 1) + r.val
        
        # 如果左右子节点都存在，递归计算它们的和；如果不存在任一子节点，则返回当前路径数值
        return (self.sumRootToLeaf(r.left, num) + self.sumRootToLeaf(r.right, num) if r.left or r.right else num) % (10 ** 9 + 7)
