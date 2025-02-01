
class Solution:
    def numberOfWays(self, num_people: int) -> int:
        """
        计算将num_people个人分成若干对的方法数。
        
        参数:
            num_people (int): 人数
        
        返回:
            int: 分法数量
        """

        self.memo = {0: 1}

        def dp(n: int) -> int:
            """
            动态规划计算n个人的分法数量.
            
            参数:
                n (int): 人数
            
            返回:
                int: 分法数量
            """
            if n not in self.memo:
                # 计算所有可能的方式，并取模10^9 + 7以防止溢出
                self.memo[n] = sum(
                    [dp(i - 2) * dp(n - i) for i in range(2, n + 1, 2)]
                ) % (10 ** 9 + 7)
            return self.memo[n]

        return dp(num_people)
