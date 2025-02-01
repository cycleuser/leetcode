
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 初始化翻转结果列表和遍历索引
    def flipMatchVoyage(self, root: 'TreeNode', voyage: list[int]) -> list[int]:
        res = []  # 存储需要翻转的节点值
        self.i = 0  # 遍历voyage数组的索引

        def dfs(node):
            if not node:
                return True  # 当前节点为空，返回True表示满足要求
            if node.val != voyage[self.i]:
                return False  # 节点值与voyage中对应位置的值不符，直接返回False
            self.i += 1  # 遍历索引后移

            # 如果左子节点存在且其值不等于voyage当前值，则交换左右子节点，并将当前节点加入结果列表
            if node.left and node.left.val != voyage[self.i]:
                node.left, node.right = node.right, node.left
                res.append(node.val)

            # 递归遍历左子树和右子树，两个条件都满足才返回True
            return dfs(node.left) and dfs(node.right)
        
        # 如果整个树满足要求则返回结果列表，否则返回[-1]
        return res if dfs(root) else [-1] 
