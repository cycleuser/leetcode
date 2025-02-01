
class Solution:
    # 定义一个类用于解决最大A值问题

    def maxA(self, N: int) -> int:
        # 初始化动态规划数组，长度为N+1
        dp = [0] * (N + 1)
        
        # 遍历所有可能的N值
        for i in range(N + 1):
            # 初始设置dp[i]=i
            dp[i] = i
            
            # 内层循环优化：只需遍历到i-3即可，因为(i-j-1)必须大于0
            for j in range(1, i - 2 + 1):  # 增加1以包含i-2的情况
                # 更新dp[i]为最大值
                dp[i] = max(dp[i], dp[j] * (i - j - 1))
                
        # 返回最终结果
        return dp[N]



class Solution:
    def maxA(self, N: int) -> int:
        dp = [0] * (N + 1)
        
        for i in range(N + 1):
            dp[i] = i
            
            for j in range(1, i - 2 + 1):  
                dp[i] = max(dp[i], dp[j] * (i - j - 1))
                
        return dp[N]
