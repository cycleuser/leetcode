
class Solution:
    def removeBoxes(self, A):
        """
        解决问题：给定一个由整数组成的列表A，从列表中移除所有元素并获取最大分数。
                   移除相同数字的连续段可得额外分数（移除一段长度为k的相同数字得(k+1)^2分）。

        参数：
            A (List[int]): 由整数组成的列表

        返回值：
            int: 最大得分
        """
        
        n = len(A)
        memo = [[[0] * n for _ in range(n)] for _ in range(n)]

        def dp(i, j, k):
            """
            动态规划函数，计算移除子数组A[i:j+1]的最大得分，其中连续相同数字k表示已经预处理的连续段。

            参数：
                i (int): 子数组起始索引
                j (int): 子数组结束索引
                k (int): 连续相同数字计数

            返回值：
                int: 移除子数组的最大得分
            """
            if i > j:
                return 0
            if not memo[i][j][k]:
                m = i
                # 寻找A[i]的连续段并合并进k中
                while m + 1 <= j and A[m+1] == A[i]:
                    m += 1
                i, k = m, k + m - i
                ans = dp(i+1, j, 0) + (k+1)**2
                # 尝试在A[i]和A[j]之间插入分界线，以获得更大得分
                for m in range(i+1, j+1):
                    if A[i] == A[m]:
                        ans = max(ans, dp(i+1, m-1, 0) + dp(m, j, k+1))
                memo[i][j][k] = ans
            return memo[i][j][k]

        return dp(0, n-1, 0)
