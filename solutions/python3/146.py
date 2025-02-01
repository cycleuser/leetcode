
class Node:  # 节点类
    def __init__(self, key, value):
        """
        初始化节点对象，设置键、值和双向链表指针。
        
        :param key: 键
        :param value: 值
        """
        self.key = key
        self.val = value
        self.next = None  # 后继节点
        self.pre = None  # 前驱节点

class LRUCache:
    def remove(self, node):
        """
        移除链表中的指定节点，并更新字典。
        
        :param node: 要移除的节点
        """
        node.pre.next, node.next.pre = node.next, node.pre
        self.dic.pop(node.key)
        
    def add(self, node):
        """
        将新节点添加到链表尾部，并更新字典。
        
        :param node: 新增节点
        """
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre.next = self.tail.pre = node
        self.dic[node.key] = node
        
    def __init__(self, capacity):
        self.dic = {}  # 存储键值对的字典
        self.n = capacity  # 缓存容量
        self.head = self.tail = Node(0, 0)  # 初始化头尾节点，用于双端链表实现缓存
        self.head.next = self.tail
        self.tail.pre = self.head
        
    def get(self, key):
        """
        获取键对应的值，并将该元素移动到链表末尾。
        
        :param key: 要获取的键
        :return: 值或-1（如果键不存在）
        """
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1
            
    def put(self, key, value):
        """
        插入新元素到缓存中，如果已存在，则更新值并移动至末尾。
        
        :param key: 键
        :param value: 值
        """
        if key in self.dic:
            self.remove(self.dic[key])
        node = Node(key, value)
        self.add(node)
        if len(self.dic) > self.n:
            self.remove(self.head.next)
