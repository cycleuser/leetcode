
class StringIterator:
    # 构造函数，初始化字符串和索引相关变量，并调用findCount方法解析第一个字符及其计数
    def __init__(self, compressedString):
        self.s, self.n = compressedString, len(compressedString)
        self.ind = self.count = self.new = 0
        self.findCount()

    # 解析字符串中的下一个数字计数值，更新ind和new指针位置
    def findCount(self):
        j = self.ind + 1
        while j < self.n and self.s[j].isnumeric(): j += 1
        self.count = int(self.s[self.ind + 1:j])  # 计算字符计数
        self.new = j                              # 更新新指针位置

    # 返回下一个字符，如果count为0且没有更多字符，则返回空格
    def next(self):
        if not self.count:
            if self.new >= self.n: return " "
            elif self.new < self.n:
                self.ind = self.new  # 将ind更新到new指针位置
                self.findCount()     # 解析下一个数字计数值

        self.count -= 1  # 减少count值，模拟字符被消费掉
        return self.s[self.ind]  # 返回当前索引指向的字符

    # 判断是否有更多字符可返回
    def hasNext(self):
        return self.count > 0 or self.new < self.n - 1
