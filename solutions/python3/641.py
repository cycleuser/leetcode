
class Node:
    """节点类，包含值和前后节点指针"""
    def __init__(self, value):
        self.val = value
        self.next = self.pre = None

class MyCircularDeque:

    def __init__(self, k: int):
        """
        初始化循环双端队列。k为最大容量。
        :param k:
        """
        # 使用虚拟头尾节点简化边界情况处理
        self.head = self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = k  # 容量
        self.curSize = 0  # 当前容量

    def add(self, value: int, preNode: 'Node'):
        """
        在指定节点后插入新节点。
        :param value: 新值
        :param preNode: 前驱节点
        """
        new_node = Node(value)
        new_node.pre = preNode
        new_node.next = preNode.next
        new_node.next.pre = new_node
        preNode.next = new_node

    def remove(self, preNode: 'Node'):
        """
        移除指定节点的后继节点。
        :param preNode: 前驱节点
        """
        node_to_remove = preNode.next
        node_to_remove.pre.next = node_to_remove.next
        node_to_remove.next.pre = node_to_remove.pre

    def insertFront(self, value: int) -> bool:
        """
        在队列头部插入值，返回是否成功。
        :param value: 要插入的值
        :return: 是否成功
        """
        if self.curSize < self.size:
            self.add(value, self.head)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        """
        在队列尾部插入值，返回是否成功。
        :param value: 要插入的值
        :return: 是否成功
        """
        if self.curSize < self.size:
            self.add(value, self.tail.pre)
            return True
        return False

    def deleteFront(self) -> bool:
        """
        删除队列头部元素，返回是否成功。
        :return: 是否成功
        """
        if self.curSize > 0:
            self.remove(self.head)
            return True
        return False

    def deleteLast(self) -> bool:
        """
        删除队列尾部元素，返回是否成功。
        :return: 是否成功
        """
        if self.curSize > 0:
            self.remove(self.tail.pre.pre)
            return True
        return False

    def getFront(self):
        """
        获取头部值。若为空，则返回-1。
        :return: 队列首部元素或-1
        """
        if self.curSize > 0:
            return self.head.next.val
        return -1

    def getRear(self):
        """
        获取尾部值。若为空，则返回-1。
        :return: 队列尾部元素或-1
        """
        if self.curSize > 0:
            return self.tail.pre.val
        return -1

    def isEmpty(self) -> bool:
        """
        检查是否为空。
        :return: 是否为空
        """
        return self.curSize == 0

    def isFull(self) -> bool:
        """
        检查是否已满。
        :return: 是否已满
        """
        return self.curSize == self.size
