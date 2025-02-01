
class RLEIterator:

    def __init__(self, A):
        """
        初始化RLE解码器，A为压缩序列，逆序存储。
        :param A: List[int] 压缩序列
        """
        self.it = A[::-1]

    def next(self, n):
        """
        获取下一个元素。解压前n个重复的值并返回实际元素。
        如果无法满足n次解压，则返回-1。
        :type n: int
        :rtype: int
        """
        while self.it and self.it[-1] <= n:
            if self.it[-1]:  # 只有当数量大于0时，才更新last值
                last = self.it[-2]
            n -= self.it.pop()  # 减去当前的数量
            self.it.pop()  # 删除当前数量

        if n and self.it:  # 如果n还有剩余且不为空
            self.it[-1] -= n  # 更新剩余的解压次数
            last = self.it[-2]
        
        return last if self.it else -1
