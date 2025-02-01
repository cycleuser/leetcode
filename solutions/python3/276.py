
class Solution:
    def numWays(self, n: int, k: int) -> int:
        """
        计算n个连续栅栏涂色的方法数，每种颜色可以重复使用。
        
        :param n: 栅栏的数量 (int)
        :param k: 可用的颜色种类 (int)
        :return: 涂色方法总数 (int)
        """
        # 初始状态：第一段栅栏的相同和不同涂色方式
        same, dif = 0, k
        
        # 动态规划计算后续栅栏的涂色方式
        for _ in range(1, n):
            same, dif = dif, (same + dif) * (k - 1)
        
        # 返回总数，考虑n为0的情况
        return same + dif if n else 0
