
class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        
        # 计算树的高度（行数）
        def traverse(node):
            if not node: 
                return 0
            return max(traverse(node.left), traverse(node.right)) * 2 + 1
        
        height = traverse(root)  # 树的高度
        
        # 初始化栈和字典，以及结果列表和当前填充长度
        stack, dic, res, padding = [root], {root : height // 2}, [], height // 2
        
        while any(stack):  # 当栈不为空时循环
            out, tmp, padding = [""] * height, [], padding // 2
            
            for i, node in enumerate(stack):
                out[dic[node]] = str(node.val)  # 填充当前层的节点值
                
                if node.left: 
                    dic[node.left] = dic[node] - padding - 1
                    tmp.append(node.left)
                
                if node.right:
                    dic[node.right] = dic[node] + padding + 1
                    tmp.append(node.right)
            
            res.append(out)  # 将当前层的结果添加到结果列表中
            stack = tmp
        
        return res  # 返回最终的层次遍历结果矩阵
