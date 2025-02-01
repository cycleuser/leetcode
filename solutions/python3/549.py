
class Solution:
    # 定义一个求最长连续序列的方法，输入是树的根节点
    def longestConsecutive(self, root):
        # 初始化递增和递减计数字典
        dec, inc = {}, {}
        
        # 使用深度优先搜索方法遍历树
        def dfs(node):
            if not node: 
                return 0
            
            # 递归左子节点，获取其递增长度
            l = dfs(node.left)
            
            # 递归右子节点，获取其递增长度
            r = dfs(node.right)
            
            # 计算当前节点的递增序列长度（考虑左子节点）
            incL = inc[node.left] + 1 if node.left and node.val == node.left.val + 1 else 1
            
            # 计算当前节点的递增序列长度（考虑右子节点）
            incR = inc[node.right] + 1 if node.right and node.val == node.right.val + 1 else 1
            
            # 更新当前节点的最大递增序列长度
            inc[node] = max(incL, incR)
            
            # 计算当前节点的递减序列长度（考虑左子节点）
            decL = dec[node.left] + 1 if node.left and node.val == node.left.val - 1 else 1
            
            # 计算当前节点的递减序列长度（考虑右子节点）
            decR = dec[node.right] + 1 if node.right and node.val == node.right.val - 1 else 1
            
            # 更新当前节点的最大递减序列长度
            dec[node] = max(decL, decR)
            
            # 如果存在左、右孩子且左右孩子分别满足递增/递减关系，则计算最大连续序列长度
            if node.left and node.right and \
               (node.left.val == node.val - 1 and node.right.val == node.val + 1) or \
               (node.left.val == node.val + 1 and node.right.val == node.val - 1):
                m = inc[node.left] + dec[node.right] + 1
            else:
                m = 0
            
            # 返回当前节点的最大连续序列长度（考虑左右子节点和自身）
            return max(m, l, r, inc[node], dec[node])
        
        # 从根节点开始进行深度优先搜索
        return dfs(root)
