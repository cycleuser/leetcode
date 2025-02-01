
class Node:
    def __init__(self, value):
        # 初始化节点，设置值和前后指针
        self.val = value
        self.next = self.pre = None

class MyLinkedList:

    def __init__(self):
        # 初始化链表头尾节点以及大小
        self.head = self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0
        
    def add(self, preNode, val):
        # 在指定节点前插入新节点
        node = Node(val)
        node.pre = preNode
        node.next = preNode.next
        node.next.pre = node.pre.next = node
        self.size += 1
        
    def remove(self, node):
        # 移除指定节点，并调整前后节点链接
        node.pre.next = node.next
        node.next.pre = node.pre
        self.size -= 1
        
    def forward(self, start, end, cur):
        # 从当前节点开始向前遍历
        while start != end:
            start += 1
            cur = cur.next
        return cur
    
    def backward(self, start, end, cur):
        # 从当前节点开始向后遍历
        while start != end:
            start -= 1
            cur = cur.pre
        return cur
    
    def get(self, index):
        # 获取指定索引位置的值，分前半部分和后半部分处理
        if 0 <= index <= self.size // 2:
            return self.forward(0, index, self.head.next).val
        elif self.size // 2 < index < self.size:
            return self.backward(self.size - 1, index, self.tail.pre).val
        return -1

    def addAtHead(self, val):
        # 在链表头部添加节点
        self.add(self.head, val)

    def addAtTail(self, val):
        # 在链表尾部添加节点
        self.add(self.tail.pre, val)

    def addAtIndex(self, index, val):
        # 在指定索引位置插入新节点，分前半部分和后半部分处理
        if 0 <= index <= self.size // 2:
            self.add(self.forward(0, index, self.head.next).pre, val)
        elif self.size // 2 < index <= self.size:
            self.add(self.backward(self.size, index, self.tail).pre, val)

    def deleteAtIndex(self, index):
        # 删除指定索引位置的节点
        if 0 <= index <= self.size // 2:
            self.remove(self.forward(0, index, self.head.next))
        elif self.size // 2 < index < self.size:
            self.remove(self.backward(self.size - 1, index, self.tail.pre))
