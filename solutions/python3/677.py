
class MapSum:

    def __init__(self):
        """
        初始化数据结构。
        """
        from collections import defaultdict
        self.dic = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        """
        插入键值对 (key, val)。
        
        :param key: str - 要插入的键
        :param val: int - 对应的值
        :return: 无返回值
        """
        self.dic[key] = val

    def sum(self, prefix: str) -> int:
        """
        计算所有以给定前缀开头的键对应的值之和。
        
        :param prefix: str - 给定的前缀
        :return: int - 符合条件的所有键对应的值之和
        """
        sm = 0
        for k in self.dic:
            if k[:len(prefix)] == prefix: 
                sm += self.dic[k]
        return sm


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
