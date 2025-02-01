
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # 定义取模常数
        mod = 10 ** 9 + 7
        
        # 初始化动态规划表，dp[i][j] 表示使用 i 个骰子达到和为 j 的方法数
        dp = [[0 for _ in range(target + 1)] for _ in range(d + 1)]
        
        # 初始状态：0 个骰子得到和为 0 的唯一方法是空操作
        dp[0][0] = 1
        
        # 动态规划填充过程
        for num_dice in range(1, d + 1):
            for face_value in range(1, f + 1):
                for sum_val in range(target - face_value + 1):  # 避免越界操作
                    dp[num_dice][sum_val + face_value] += dp[num_dice - 1][sum_val]
                    dp[num_dice][sum_val + face_value] %= mod
        
        # 返回结果：使用 d 个骰子达到和为 target 的方法数
        return dp[d][target]
