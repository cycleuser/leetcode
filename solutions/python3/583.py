
class Solution:
    # Python solution to find minimum distance between two strings

    def minDistance(self, w1: str, w2: str) -> int:
        """
        计算两个字符串的最小编辑距离
        
        :param w1: 第一个字符串
        :param w2: 第二个字符串
        :return: 最小编辑距离
        """

        m, n = len(w1), len(w2)
        
        # 创建动态规划表
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 初始化边界条件
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = i + j
                elif w1[i - 1] == w2[j - 1]:
                    # 如果字符相同，不需要编辑操作
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # 计算插入、删除或替换的最小编辑距离
                    dp[i][j] = min(dp[i][j - 1] + 1, dp[i - 1][j] + 1)
        
        # 返回最终结果
        return dp[-1][-1]
