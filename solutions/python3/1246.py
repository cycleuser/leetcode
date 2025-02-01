
class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        """
        计算最小移动次数使得数组中的元素相等
        
        参数:
            arr (List[int]): 输入的整数列表
        
        返回值:
            int: 使数组中所有元素相等所需的最小移动次数
        """
        
        n = len(arr)           # 数组长度
        dp = [[0] * (n + 1) for _ in range(n + 1)]    # 动态规划表，初始化为全零
        
        for l in range(1, n + 1):   # 遍历子数组的长度
            i, j = 0, l - 1         # 子数组左右边界
            
            while j < n:            # 确保右边界在数组范围内
                if l == 1:
                    dp[i][j] = 1    # 单个元素不需要移动
                
                else:
                    # 计算当前子数组的最小移动次数
                    dp[i][j] = 1 + dp[i + 1][j]
                    
                    if arr[i] == arr[i + 1]:   # 检查首尾元素是否相等
                        dp[i][j] = min(1 + dp[i + 2][j], dp[i][j])     # 动态规划转移方程
                
                    for k in range(i + 2, j + 1):
                        if arr[i] == arr[k]:   # 检查是否存在相等元素
                            dp[i][j] = min(dp[i + 1][k - 1] + dp[k + 1][j], dp[i][j])     # 动态规划转移方程
                
                i, j = i + 1, j + 1   # 移动左右边界
        
        return dp[0][n - 1]       # 返回最终结果
