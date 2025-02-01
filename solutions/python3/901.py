    
class StockSpanner:

    def __init__(self):
        """
        初始化类实例，用于存储股票价格序列和对应的权重。
        
        :初始化: 两个列表arr和res，分别存放价格序列和权重序列。
        """
        self.arr = []
        self.res = []

    def next(self, price):
        """
        添加一个新的股票价格，并返回该价格的权重。

        :type price: int
        :rtype: int
        """
        if self.arr and self.arr[-1] > price:
            self.res.append(1)
        else:
            i = len(self.arr) - 1
            while i >= 0:
                if self.arr[i] <= price and self.res[i]:
                    i -= self.res[i]
                else:
                    break
            self.res.append(len(self.arr) - i)
        self.arr.append(price)
        return self.res[-1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
