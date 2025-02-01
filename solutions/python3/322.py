
class Solution:
    # 定义一个求硬币组合问题的方法，输入为可选硬币列表和目标金额
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        :type coins: List[int]  # 硬币面值列表
        :type amount: int       # 目标金额
        :rtype: int             # 返回最少硬币数量或-1（表示无法构成目标金额）
        """

        # 初始化动态规划表，dp[i] 表示凑成 i 元所需的最小硬币数，默认为正无穷大
        dp = [0] + [float('inf')] * amount

        # 遍历从 1 到目标金额的每种可能值
        for i in range(1, amount + 1):
            # 尝试使用不同面值硬币凑成当前金额，选择最小的硬币数
            dp[i] = min([dp[i - c] if i - c >= 0 else float('inf') for c in coins]) + 1

        # 如果最终结果仍为正无穷大，则表示无法构成目标金额；否则返回所需最少硬币数量
        return dp[amount] if dp[amount] != float('inf') else -1
