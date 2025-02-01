
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 寻找二叉树的每层最外侧节点
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res = []
        
        # 深度优先搜索，返回当前节点所在层数
        def dfs(node):
            if not node: 
                return -1  # 空节点标记为-1
            
            i = max(dfs(node.left), dfs(node.right)) + 1  # 计算左右子树的最大深度并加1
            
            try:
                res[i].append(node.val)  # 尝试在对应层数的列表中添加当前节点值
            except IndexError:
                res.append([node.val])  # 如果越界则创建新列表
            
            return i
        
        dfs(root)
        
        return res
