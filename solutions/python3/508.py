
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 寻找二叉树中频率最高的子树和
    def findFrequentTreeSum(self, root: 'TreeNode') -> 'List[int]':
        if not root:
            return []  # 如果根节点为空，返回空列表
        
        def traverse(node):
            # 遍历每个节点，计算以该节点为根的子树的和
            if not node:
                return 0
            sm = traverse(node.left) + traverse(node.right) + node.val
            if sm in dic:
                dic[sm] += 1
            else:
                dic[sm] = 1
            return sm
        
        # 使用字典记录每个子树和出现的频率
        dic = {}
        traverse(root)
        
        # 找出最高频次
        mx = max(dic.values())
        
        # 返回最高频次的所有子树和
        return [k for k in dic.keys() if dic[k] == mx]
