
class BSTIterator:
    # 初始化迭代器，传入根节点
    def __init__(self, root: 'TreeNode'):
        self.stack = []
        self.pushAll(root)

    # 返回二叉搜索树中的下一个最小的数
    def next(self) -> int:
        cur = self.stack.pop()
        self.pushAll(cur.right)
        return cur.val

    # 判断迭代器中是否还有节点
    def hasNext(self) -> bool:
        return len(self.stack) > 0

    # 将当前节点的所有左子节点压入栈中
    def pushAll(self, node):
        while node != None:
            self.stack.append(node)
            node = node.left
