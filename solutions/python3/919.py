
class CBTInserter:

    # 初始化，构建自底向上的完全二叉树表示
    def __init__(self, root):
        from collections import deque
        self.arr, q = [], deque([root])
        while q:
            for node in q:
                self.arr.append(node)
            q.extend(child for node in q if (child := getattr(node, 'left', None) or getattr(node, 'right', None)))

    # 插入节点，返回插入节点的父节点值
    def insert(self, v):
        parent = self.arr[(len(self.arr) - 1) // 2]
        child = TreeNode(v)
        if not len(self.arr) % 2:
            parent.right = child
        else:
            parent.left = child
        self.arr.append(child)
        return parent.val

    # 获取根节点
    def get_root(self):
        return self.arr[0]
