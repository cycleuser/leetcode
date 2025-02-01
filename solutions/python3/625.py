
class Solution:
    def smallestFactorization(self, a):
        """
        获取a的最小因子分解结果。
        
        参数:
            a (int): 需要进行因子分解的整数
        
        返回:
            int: 最小因子分解的结果，若无有效解则返回0
        """

        res = []

        def dfs(num):
            """
            深度优先搜索实现最小因子分解。

            参数:
                num (int): 当前待分解的数字
            
            返回:
                bool: 若成功找到因子则返回True，否则返回False
            """
            if num == 1:
                return True
            for n in range(9, 1, -1):
                if not num % n:
                    res.append(str(n))
                    return dfs(num // n)
            return False

        bol, num = dfs(a), int("".join(sorted(res))) if res else 1
        return num if bol and -(2 ** 31) <= num <= 2 ** 31 - 1 else 0
