
class Node:
    # 节点类，用于构建循环双向链表的节点
    def __init__(self, value):
        self.val = value       # 节点值
        self.next = None       # 下一个节点引用
        self.pre = None        # 前一个节点引用

class MyCircularQueue:

    def __init__(self, k: int):  # 初始化循环队列，大小为k
        """
        :param k: 队列的最大容量
        """
        self.size = k            # 最大容量
        self.curSize = 0         # 当前元素数量
        self.head = Node(-1)     # 头哨兵节点
        self.tail = Node(-1)     # 尾哨兵节点
        self.head.next = self.tail   # 构建循环链表结构
        self.tail.pre = self.head

    def enQueue(self, value: int) -> bool:
        """
        向队列尾部插入一个元素，返回操作是否成功
        :param value: 要插入的值
        :return: 操作是否成功
        """
        if self.curSize < self.size:
            node = Node(value)
            # 将新节点连接到链表中
            node.pre = self.tail.pre
            node.next = self.tail
            node.pre.next = node.next.pre = node
            self.curSize += 1
            return True
        return False

    def deQueue(self) -> bool:
        """
        从队列头部移除一个元素，返回操作是否成功
        :return: 操作是否成功
        """
        if self.curSize > 0:
            node = self.head.next
            # 移除节点并更新指针
            node.pre.next = node.next
            node.next.pre = node.pre
            self.curSize -= 1
            return True
        return False

    def Front(self) -> int:
        """
        获取队列头部元素，如果为空返回 -1
        :return: 队列头部元素或-1
        """
        return self.head.next.val if not self.isEmpty() else -1

    def Rear(self) -> int:
        """
        获取队列尾部元素，如果为空返回 -1
        :return: 队列尾部元素或-1
        """
        return self.tail.pre.val if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        """
        判断队列是否为空
        :return: 是否为空
        """
        return self.curSize == 0

    def isFull(self) -> bool:
        """
        判断队列是否已满
        :return: 是否已满
        """
        return self.curSize == self.size
