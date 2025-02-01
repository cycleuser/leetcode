
class Solution:
    def maxSumDivThree(self, nums: List[int], dp: list = [0, -float("inf"), -float("inf")]) -> int:
        """
        :param nums: 输入的整数列表
        :param dp: 动态规划数组，初始化为[0, -inf, -inf]
        :return: 最大和，该和能被3整除

        思路：
        1. 使用动态规划解决。
        2. `dp[i]` 表示从前 i 个数中选取一些数（可能为空）得到的和能够被3除后余i的最大值。
        """
        for num in nums:
            # 更新dp数组
            dp = [max(dp[i], dp[(i - num) % 3] + num) for i in range(3)]
        
        return dp[0]
