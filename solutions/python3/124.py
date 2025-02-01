
class Solution:
    def maxPathSum(self, root):
        # 初始化结果为负无穷，用于存储最大路径和
        res = [-float("inf")]
        
        # 定义深度优先搜索函数
        def dfs(node):
            if not node: 
                # 如果节点为空，返回-无穷
                return -float("inf")
            
            l, r = dfs(node.left), dfs(node.right)
            # 计算以当前节点为根的最大路径和
            mx = max(node.val, l + node.val, r + node.val)
            # 更新全局最大路径和
            res[0] = max(res[0], mx, node.val + l + r)
            # 返回包含单边子树的最大路径和
            return mx
        
        # 从根节点开始深度优先搜索
        dfs(root)
        
        # 返回计算得到的最大路径和
        return res[0]
