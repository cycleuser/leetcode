
class Node:
    def __init__(self, s, e):
        """
        初始化节点类，用于二叉树结构。
        
        :param s: 起始时间
        :param e: 结束时间
        """
        self.e = e  # 结束时间
        self.s = s  # 开始时间
        self.left = None  # 左子节点
        self.right = None  # 右子节点

class MyCalendar:

    def __init__(self):
        """
        初始化日历类。
        
        :param root: 根节点，初始为空
        """
        self.root = None

    def book_helper(self, s, e, node):
        """
        辅助函数用于递归地在二叉树中预定时间。

        :param s: 起始时间
        :param e: 结束时间
        :param node: 当前节点
        :return: 是否成功预定，True表示成功，False表示失败
        """
        if s >= node.e:
            # 如果新预定的结束时间在当前节点开始时间之后
            if node.right:
                # 有右子节点则递归检查右子树
                return self.book_helper(s, e, node.right)
            else:
                # 没有右子节点，创建一个并返回成功标志
                node.right = Node(s, e)
                return True
        elif e <= node.s:
            # 如果新预定的开始时间在当前节点结束时间之前
            if node.left:
                # 有左子节点则递归检查左子树
                return self.book_helper(s, e, node.left)
            else:
                # 没有左子节点，创建一个并返回成功标志
                node.left = Node(s, e)
                return True
        else: 
            return False  # 时间冲突

    def book(self, start, end):
        """
        预定时间。

        :type start: int 起始时间
        :type end: int 结束时间
        :rtype: bool 返回是否成功预定
        """
        if not self.root:
            # 如果根节点为空，初始化树并返回成功标志
            self.root = Node(start, end)
            return True
        return self.book_helper(start, end, self.root)


# 示例用法：
# obj = MyCalendar()
# param_1 = obj.book(start, end)  # 预定时间
