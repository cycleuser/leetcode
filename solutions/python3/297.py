
class Codec:

    def serialize(self, root):
        """
        序列化二叉树，将二叉树转换为字符串形式。
        
        参数:
            root (TreeNode): 二叉树的根节点
        
        返回:
            str: 表示二叉树的字符串
        """
        q, s = root and collections.deque([root]), ""
        while q:
            node = q.popleft()
            if node is None:
                s += "null#"
            else:
                s += str(node.val) + "#"
                q += [node.left, node.right]
        return s

    def deserialize(self, data):
        """
        反序列化字符串，将字符串转换为二叉树。
        
        参数:
            data (str): 表示二叉树的字符串
        
        返回:
            TreeNode: 重构后的二叉树根节点
        """
        if not data:
            return None
        data = collections.deque(data.split("#"))
        q, root = collections.deque([TreeNode(int(data.popleft()))]), None
        while q:
            node = q.popleft()
            if not root:
                root = node
            l, r = data.popleft(), data.popleft()
            if l != "null":
                node.left = TreeNode(int(l))
                q.append(node.left)
            if r != "null":
                node.right = TreeNode(int(r))
                q.append(node.right)
        return root
