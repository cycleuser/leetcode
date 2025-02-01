
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 寻找二叉树中的众数
    def findMode(self, root: TreeNode) -> List[int]:
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        from collections import Counter
        
        # 递归遍历函数，统计节点值出现的次数
        def traverse(node):
            if node:
                dic[node.val] += 1
                traverse(node.left)
                traverse(node.right)
        
        # 初始化计数器
        dic = collections.Counter()
        # 开始遍历
        traverse(root)
        
        # 获取最大频率
        mx = max(dic.values(), default=0)
        
        # 返回所有出现频率等于最大频率的节点值
        return [k for k, v in dic.items() if v == mx]
