
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        # 使用动态规划计算k逆序对个数
        # Dynamic Programming to calculate the number of k inverse pairs
        
        dp = [1] + [0] * k  # 初始化dp数组，dp[0]=1表示没有元素时逆序对为0种情况
        
        for i in range(2, n + 1):  # 遍历n的取值
            for j in range(1, k + 1): 
                dp[j] += dp[j - 1]  # 状态转移方程的第一部分，累加前一个状态
                
            for j in range(k, 0, -1): 
                dp[j] -= (j - i >= 0 and dp[j - i])  # 状态转移方程的第二部分，减去超出范围的部分
        
        return dp[-1] % (10 ** 9 + 7)  # 返回结果，并取模
