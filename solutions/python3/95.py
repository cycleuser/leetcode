
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 生成1到n的二叉搜索树
    def generateTrees(self, n: int) -> List[TreeNode]:
        # 深度优先搜索，构造以m为根节点的子树
        def dfs(l, r):
            if r < l: 
                return [None]  # 边界条件：空节点
        
            arr = []
            for m in range(l, r + 1):  # 枚举每一个可能的根节点值
                left = dfs(l, m - 1)   # 左子树的所有情况
                right = dfs(m + 1, r)  # 右子树的所有情况
                
                for lNode in left:
                    for rNode in right: 
                        new_tree = TreeNode(m)  # 构造新的根节点
                        new_tree.left = lNode   # 左子树连接到新节点
                        new_tree.right = rNode  # 右子树连接到新节点
                        
                        arr.append(new_tree)  # 收集所有可能的树结构
            return arr
        
        result = dfs(1, n)
        
        # 如果结果中只有一个空节点，返回空列表；否则返回所有的树结构
        return [] if result == [None] else result
