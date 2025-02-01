
class Node:
    # 节点类，包含键值对、前后节点指针
    def __init__(self, key, value):
        self.val = value  # 值
        self.key = key    # 键
        self.next = None  # 后一个节点
        self.pre = None   # 前一个节点

class AllOne:
    # 包含键值对操作的数据结构
    
    def __init__(self):
        # 初始化双向链表的头尾哨兵节点以及键值映射字典
        self.first = {}  # 小于等于当前值的第一个节点
        self.last = {}   # 大于等于当前值的最后一个节点
        self.keys = {}   # 键到节点的映射
        self.head = Node(-1, -1)  # 双向链表头哨兵
        self.tail = Node(-1, -1)  # 双向链表尾哨兵
        self.head.next = self.tail  # 头尾相连形成循环链表
        self.tail.pre = self.head

    def add(self, prev, node):
        # 将节点添加到双向链表中
        node.pre = prev
        node.next = prev.next
        node.pre.next = node.next.pre = node

    def remove(self, node):
        # 从双向链表中移除节点
        node.pre.next = node.next
        node.next.pre = node.pre

    def process(self, node):
        if self.last[node.val] == node and node.pre.val != node.val:
            self.first.pop(node.val)
            self.last.pop(node.val)   # 处理当前节点为链表尾部且前后键值不相等的情况
        elif self.first[node.val] == node:
            self.first[node.val] = node.next  # 更新第一个节点的映射
        elif self.last[node.val] == node:
            self.last[node.val] = node.pre    # 更新最后一个节点的映射

    def process2(self, node, prev, key, d):
        if key in self.keys:
            if node.val + d in self.last:
                self.add(self.last[node.val + d], node)  # 增加操作：将节点添加到下一个链表位置
            elif node.val in self.last:
                self.add(self.last[node.val], node)
            else:
                self.add(prev, node)    # 处理边界情况
        elif 1 in self.last:           # 初始化操作（最小值）
            node = Node(key, 0)
            self.add(self.last[1], node)
        else:
            node = Node(key, 0)
            self.add(self.head, node)
        node.val += d    # 更新节点的值
        self.last[node.val] = node  # 更新当前最大值的映射
        if node.val not in self.first:
            self.first[node.val] = node  # 初始化当前最小值的映射
        if key not in self.keys:       # 键到节点初始化映射
            self.keys[key] = node
            
    def inc(self, key):
        if key in self.keys:
            node = self.keys[key]
            prev = node.pre
            self.process(node)
            self.remove(node)   # 当键值存在于字典中时，增加操作的处理流程
            self.process2(node, prev, key, 1)
        else:
            self.process2(None, None, key, 1)

    def dec(self, key):
        if key in self.keys:
            node = self.keys[key]
            prev = node.pre
            self.process(node)
            self.remove(node)   # 当键值存在于字典中时，减少操作的处理流程
            if node.val != 1:   # 判断当前节点是否为最小值（val=1）
                self.process2(node, prev, key, -1)
            else:
                self.keys.pop(key)
        else:
            pass

    def getMaxKey(self):
        return self.tail.pre.key if self.tail.pre != self.head else ""  # 获取最大键

    def getMinKey(self):
        return self.head.next.key if self.head.next != self.tail else ""  # 获取最小键
