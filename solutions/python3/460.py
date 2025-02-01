
class Node:
    # 节点类，用于构建双向链表中的节点
    def __init__(self, k, v, f):
        self.key = k  # 键
        self.val = v  # 值
        self.freq = f  # 频次
        self.next = None  # 下一个节点
        self.pre = None  # 上一个节点

class LFUCache:
    def __init__(self, capacity):
        """
        初始化LFU缓存类
        :param capacity: 缓存的最大容量
        """
        self.max = capacity  # 最大容量
        self.cache = 0  # 当前缓存数量
        self.freqLast = {}  # 按照频次组织的节点尾部指针字典，用于快速找到每个频次下的最后一个节点
        self.Nodes = {}  # 存储key到Node对象的映射
        self.head = self.tail = Node("#", "#", "#")  # 头尾哨兵节点
        self.head.next = self.tail  # 尾节点指向头节点
        self.tail.pre = self.head  # 头节点指向尾节点

    def changeFreq(self, key):
        """
        更新节点的频次，并调整双向链表结构
        :param key: 节点键值
        """
        node, f = self.Nodes[key], self.Nodes[key].freq  # 获取节点及其当前频次
        if self.freqLast[f] == node:
            if node.pre.freq == f:
                self.freqLast[f] = node.pre
            else:
                self.freqLast.pop(f)
        if (f + 1) in self.freqLast:
            node.pre.next = node.next
            node.next.pre = node.pre
            node.pre = self.freqLast[f + 1]
            node.next = node.pre.next
        elif f in self.freqLast:
            node.pre.next = node.next
            node.next.pre = node.pre
            node.pre = self.freqLast[f]
            node.next = node.pre.next
        node.pre.next = node.next.pre = node
        self.freqLast[f + 1] = node
        node.freq += 1

    def removeFirst(self):
        """
        移除并返回最不常用的节点
        """
        node, f = self.head.next, self.head.next.freq  # 获取头节点的下一个节点及其频次
        node.pre.next = node.next  # 调整前一个节点和后一个节点的关系，跳过当前要移除的节点
        node.next.pre = node.pre
        self.Nodes.pop(node.key)  # 移除缓存中的键值对
        if self.freqLast[f] == node:
            self.freqLast.pop(f)
        self.cache -= 1

    def get(self, key):
        """
        获取指定key对应的value，如果存在则更新节点的频次
        :param key: 键值
        :return: 对应值或-1（未找到）
        """
        if key in self.Nodes:
            self.changeFreq(key)
            return self.Nodes[key].val  # 返回节点的值，并更新其频次
        return -1

    def put(self, key, value):
        """
        插入新的键值对或更新现有键值对
        :param key: 键值
        :param value: 值
        """
        if key in self.Nodes:
            self.changeFreq(key)
            self.Nodes[key].val = value  # 更新节点的值并增加其频次
        elif self.max:
            if self.cache == self.max:
                self.removeFirst()  # 如果缓存已满，移除最不常用的节点
            self.cache += 1
            new = Node(key, value, 1)  # 创建新的节点
            if 1 in self.freqLast:
                new.pre = self.freqLast[1]
            else:
                new.pre = self.head
            new.next = new.pre.next
            new.pre.next = new.next.pre = new
            self.freqLast[1] = self.Nodes[key] = new  # 将新节点添加到链表中，并更新缓存字典
