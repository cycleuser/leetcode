
class Solution:
    # 检查给定的二叉树是否为完全二叉树
    def isCompleteTree(self, root):
        # 使用队列进行层次遍历，同时标记节点结束位置
        q, pre = [root, None], 1
        
        while any(q):  # 遍历队列中的所有元素直到为空
            i = q.index(None)  # 找到第一个None的位置
            
            if any(q[i:]) or pre > 1:  # 如果后面还有非空节点或之前标记了多个结束点，返回False
                return False
            
            pre = len(q[i:])  # 更新上一个None后的节点数
            
            q = [child for node in q[:i] for child in (node.left, node.right)] + [None]  # 展平子树并添加新的None标记
        
        return True  # 如果没有违反完全二叉树规则，返回True
