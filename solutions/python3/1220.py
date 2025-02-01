
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """
        计算n个字母的元音排列数量，结果对10^9 + 7取模。

        参数：
            n (int): 字母的数量

        返回值：
            int: 元音排列的数量
        """
        mod = 10 ** 9 + 7
        
        # dp[i] 表示以第 i 个元音结尾的字符串数量（i=0:a, i=1:e, i=2:i, i=3:o, i=4:u）
        dp = [1] * 5

        for _ in range(n - 1):
            # 初始化下一状态数组
            add = [0] * 5
            
            # 计算以 'a' 结尾的字符串数量，仅由上一状态 'e' 转换而来
            add[1] = (add[1] + dp[0]) % mod

            # 计算以 'e' 结尾的字符串数量，可以由 'a' 或 'i' 转换而来
            add[0] = (add[0] + dp[1]) % mod
            add[2] = (add[2] + dp[1]) % mod

            # 计算以 'i' 结尾的字符串数量，可以由 'e', 'o', 或 'u' 转换而来
            add[0] = (add[0] + dp[2]) % mod
            add[1] = (add[1] + dp[2]) % mod
            add[3] = (add[3] + dp[2]) % mod
            add[4] = (add[4] + dp[2]) % mod

            # 计算以 'o' 结尾的字符串数量，可以由 'i' 转换而来
            add[2] = (add[2] + dp[3]) % mod
            add[4] = (add[4] + dp[3]) % mod

            # 计算以 'u' 结尾的字符串数量，仅由上一状态 'i' 转换而来
            add[0] = (add[0] + dp[4]) % mod
            
            # 更新当前状态为下一状态
            for i in range(5):
                dp[i] = add[i] % mod

        return sum(dp) % mod
