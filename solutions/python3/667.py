
class Solution:
    def constructArray(self, n: int, k: int) -> list[int]:
        """
        构造一个长度为n的数组，使得相邻元素之差尽可能大。
        
        :param n: 数组长度
        :param k: 最大允许的最大差值次数
        :return: 满足条件的数组
        """
        left, right, res = 0, n+1, [None]*n
        for i in range(n):
            # 如果最大差值k已经用完，填充剩余位置为递增序列
            if k == 1:
                if i % 2 == 0:
                    while i < n: 
                        res[i], right, i = right - 1, right - 1, i + 1 
                else:
                    while i < n: 
                        res[i], left, i = left + 1, left + 1, i + 1
                return res
            
            # 否则根据i的奇偶性填充数组，同时减少k值
            if i % 2 != 0: 
                res[i], right = right - 1, right - 1
            else: 
                res[i], left = left + 1, left + 1
            k -= 1
