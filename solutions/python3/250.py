
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 计算单值子树的数量
    def countUnivalSubtrees(self, root):
        res = [0]  # 存储结果
        
        # 深度优先搜索，判断节点是否为单值子树
        def dfs(node, value):
            if not node:  # 空节点返回True和默认的值
                return True, value
            
            left, lVal = dfs(node.left, node.val)  # 处理左子树
            right, rVal = dfs(node.right, node.val)  # 处理右子树
            
            cnt = left and right and lVal == rVal == node.val  # 判断当前节点及其子树是否为单值子树
            if cnt:
                res[0] += 1  # 更新结果计数器
            
            return cnt, node.val  # 返回判断结果和当前节点的值
        
        dfs(root, None)  # 从根节点开始深度优先搜索
        return res[0]  # 返回最终的结果
