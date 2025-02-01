
class Node:
    # 节点类，用于存储值和索引，并提供指向前驱和后继节点的引用
    def __init__(self, value, index):
        self.val = value  # 值
        self.i = index    # 索引
        self.pre = None   # 前驱节点
        self.next = None  # 后继节点

class MaxStack:
    
    def __init__(self):
        """
        初始化数据结构。
        """
        self.heap = []         # 最大堆，用于快速获取最大值
        self.Nodes = {}        # 字典，存储节点以快速查找
        self.head = Node(0, -1)  # 头节点
        self.tail = Node(0, -2)  # 尾节点
        self.head.next = self.tail  # 链表连接
        self.tail.pre = self.head

    def push(self, x):
        """
        :type x: int
        :rtype: void
        在链表尾部插入新节点，并在堆中插入对应元组 (-x, -i)。
        """
        newNode = Node(x, self.tail.pre.i + 1)
        newNode.pre = self.tail.pre
        newNode.next = self.tail
        self.tail.pre.next = self.tail.pre = newNode
        self.Nodes[newNode.i] = newNode
        heapq.heappush(self.heap, (-x, -newNode.i))

    def pop(self):
        """
        :rtype: int
        删除尾部节点，并在堆中移除对应元组。
        """
        node = self.tail.pre
        node.pre.next = self.tail
        self.tail.pre = node.pre
        self.Nodes.pop(node.i)
        if node.i == -self.heap[0][1]:
            heapq.heappop(self.heap)
        return node.val

    def top(self):
        """
        :rtype: int
        返回尾部节点的值。
        """
        return self.tail.pre.val

    def peekMax(self):
        """
        :rtype: int
        调整堆以确保最大值在堆顶，返回最大值（若无效则抛出异常）。
        """
        while -self.heap[0][1] not in self.Nodes or self.Nodes[-self.heap[0][1]].val != -self.heap[0][0]:
            heapq.heappop(self.heap)
        return -self.heap[0][0]

    def popMax(self):
        """
        :rtype: int
        移除堆顶元素对应的节点，并调整链表以移除该节点。
        返回最大值（若无效则抛出异常）。
        """
        while -self.heap[0][1] not in self.Nodes or self.Nodes[-self.heap[0][1]].val != -self.heap[0][0]:
            heapq.heappop(self.heap)
        node = self.Nodes.pop(-self.heap[0][1])
        node.pre.next = node.next
        node.next.pre = node.pre
        return -heapq.heappop(self.heap)[0]
