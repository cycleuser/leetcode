
class Solution:
    def connect(self, root: "Node") -> "Node":
        """
        连接二叉树中的节点，每个节点需指向其下一个右侧节点。

        参数:
            root (Node): 二叉树的根节点

        返回值:
            Node: 修改后的根节点
        """
        if root == None:
            return root
        
        # 使用队列进行层次遍历，并记录上一个处理的节点及其层级位置
        q, prev = [(root, 1)], None
        while q:
            curr, pos = q.pop(0)
            
            # 如果当前节点不是第一个处理的节点，则连接prev和当前节点
            if prev != None and prev[1] == pos:
                prev[0].next = curr
            
            prev = [curr, pos]
            
            # 将左右子节点及其层级位置加入队列
            if curr.left:
                q.append((curr.left, pos + 1))
            if curr.right:
                q.append((curr.right, pos + 1))
        
        return root
